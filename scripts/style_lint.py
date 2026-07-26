#!/usr/bin/env python3
"""Style linter for the CTB Admin documentation.

Enforces the rules in `.github/STYLE_SPEC.md` that no other tool checks.
mdformat covers Markdown formatting and `main.py nav-audit` covers navigation;
this covers page structure, heading vocabulary, terminology, and voice.

Usage:
    uv run python scripts/style_lint.py                  # lint docs/user-guide
    uv run python scripts/style_lint.py --no-baseline    # ignore the baseline
    uv run python scripts/style_lint.py --update-baseline
    uv run python scripts/style_lint.py --stats
    uv run python scripts/style_lint.py --report-unverified

Baseline
--------
Known violations are recorded in `scripts/style_lint_baseline.json` so the gate
can be switched on before every page has been rewritten. Only *new* violations
fail the build. Shrinking the baseline to zero is the goal; it can never grow
without an explicit `--update-baseline`.

Per-file escape hatch, for the rare legitimate exception:

    <!-- style-lint: allow=heading-case,terminology -->
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

DOCS_ROOT = Path("docs/user-guide")
BASELINE_PATH = Path("scripts/style_lint_baseline.json")

# ---------------------------------------------------------------------------
# Spec constants (.github/STYLE_SPEC.md)
# ---------------------------------------------------------------------------

# Section 3 — canonical page template, in required order.
CANONICAL_SECTIONS = [
    "Summary",
    "When to use this page",
    "How to access this page",
    "Prerequisites",
    "Step-by-step instructions",
    "Field reference",
    "Tips and common issues",
    "Related pages",
]
MANDATORY_SECTIONS = [
    "Summary",
    "When to use this page",
    "How to access this page",
    "Step-by-step instructions",
    "Field reference",
    "Related pages",
]
# Module landing pages (README.md) describe a section rather than a task.
MODULE_SECTIONS = [
    "Summary",
    "What you can do in this module",
    "Pages in this module",
    "Typical workflow",
    "Related pages",
]
MODULE_MANDATORY = MODULE_SECTIONS

# A heading that opens with one of these stems must match a canonical section
# exactly. Catches "When to use Generate Salary page" and friends.
CANONICAL_STEMS = [
    "Summary",
    "When to use",
    "How to access",
    "Prerequisite",
    "Step-by-step",
    "Step by step",
    "Field reference",
    "Tips and",
    "Related page",
]

# Section 4.2 — the only approved admonition types.
APPROVED_ADMONITIONS = {"info", "tip", "warning", "note"}

# Section 5 — terminology glossary.
FORBIDDEN_TERMS = {
    r"\bcustomers?\b": "Client",
    r"\bbuyers?\b": "Client",
    r"\bsuppliers?\b": "Vendor",
    r"\bsellers?\b": "Vendor",
    # Not "bill-of-materials", which is a manufacturing term, not an invoice.
    r"(?<!-)\bbills?\b(?!-)": "Invoice",
    r"\bdisbursements?\b": "Payout",
    r"\bpaychecks?\b": "Salary",
    r"\bjournal entr(y|ies)\b": "Voucher",
    r"\bleft menu\b": "Sidebar",
    r"\bnavigation panel\b": "Sidebar",
    r"\bhome screen\b": "Dashboard",
}

# Section 6.2 — nav labels. The UI paths in the docs must match them.
FORBIDDEN_MODULE_LABELS = {
    r"\bTrade Management\b": "Trade",
    r"\bEmployee Management\b": "Employee",
    r"\bBusiness Management\b": "Business",
    r"\bFactory Management\b": "Factory",
    r"\bSettings Management\b": "Settings and Admin",
}

# Section 2 — prohibited phrases.
PROHIBITED_PHRASES = {
    r"\bsimply\b": "delete the word",
    r"\bjust\b": "delete the word",
    r"\beasily\b": "delete the word",
    r"\bstraightforward\b": "delete the word",
    r"\bseamless(ly)?\b": "delete the word",
    r"\bleverag(e|es|ing)\b": "use",
    r"\butiliz(e|es|ing)\b": "use",
    r"\bnavigate to\b": "Go to / Open",
    r"\bit is worth noting\b": "delete the phrase",
    r"\bit should be noted\b": "delete the phrase",
    r"\bnote that\b": "delete the phrase",
    r"\ballows? you to\b": "rewrite in the imperative",
    # Third person where the reader is meant ("Users can filter" -> "You can
    # filter"). Anchored to the start of a sentence or list item on purpose:
    # in admin documentation "the user" routinely means a managed account
    # rather than the reader, and "the user avatar" is a UI element.
    r"^\s*[-*]?\s*(The )?[Uu]sers? (can|should|must|need to)\b": "address the reader as 'you'",
    r"\bplease\b": "delete the word",
}

# Words that may legitimately stay capitalised mid-heading: product terms and
# on-screen UI labels. Extend this rather than weakening the heading-case rule.
UI_PROPER_NOUNS = {
    "ctb",
    "admin",
    "client",
    "clients",
    "vendor",
    "vendors",
    "invoice",
    "invoices",
    "quotation",
    "tender",
    "chalan",
    "payment",
    "payments",
    "check",
    "checks",
    "voucher",
    "vouchers",
    "bank",
    "banks",
    "employee",
    "employees",
    "salary",
    "salaries",
    "wage",
    "wages",
    "payout",
    "payouts",
    "attendance",
    "department",
    "departments",
    "position",
    "positions",
    "task",
    "tasks",
    "product",
    "products",
    "material",
    "materials",
    "category",
    "categories",
    "inventory",
    "dashboard",
    "sidebar",
    "quran",
    "sms",
    "nid",
    "sku",
    "id",
    "url",
    "api",
    "pwa",
}

TAG_NAMESPACES = {"module", "task", "role"}
TAG_VALUES = {
    "module": {
        "getting-started",
        "business",
        "factory",
        "trade",
        "employee",
        "returns",
        "commission",
        "reports",
        "settings",
        "reference",
    },
    "task": {"create", "edit", "view", "report", "configure", "troubleshoot"},
    "role": {"staff", "accountant", "hr", "admin"},
}

PLACEHOLDER_STRINGS = [
    "Description placeholder",
    "Required permissions or existing records may be needed",
    "Use the available filters and actions to manage the workflow",
    "Field name** — Description",
]

HR = "_" * 70

# ---------------------------------------------------------------------------

ALLOW_RE = re.compile(r"<!--\s*style-lint:\s*allow=([a-z0-9,\-\s]+)\s*-->")
ADMONITION_RE = re.compile(
    r"^(?P<indent>\s*)!!!(?P<space>\s*)(?P<type>\S+)(?P<rest>.*)$"
)
HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<text>.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


@dataclass(frozen=True)
class Violation:
    path: str
    line: int
    rule: str
    message: str

    def key(self) -> str:
        return f"{self.path}::{self.rule}"

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: [{self.rule}] {self.message}"


class PageLinter:
    def __init__(self, path: Path, text: str) -> None:
        self.path = path
        self.rel = path.as_posix()
        self.text = text
        self.lines = text.splitlines()
        self.allowed = self._allowed_rules()
        self.is_module_page = path.name == "README.md"
        self.code_lines = self._code_line_mask()
        self.violations: list[Violation] = []

    # -- helpers ------------------------------------------------------------

    def _allowed_rules(self) -> set[str]:
        allowed: set[str] = set()
        for match in ALLOW_RE.finditer(self.text):
            allowed |= {r.strip() for r in match.group(1).split(",") if r.strip()}
        return allowed

    def _code_line_mask(self) -> set[int]:
        """Line numbers (0-based) inside fenced code blocks."""
        inside = False
        masked: set[int] = set()
        for i, line in enumerate(self.lines):
            if FENCE_RE.match(line):
                inside = not inside
                masked.add(i)
                continue
            if inside:
                masked.add(i)
        return masked

    def add(self, line: int, rule: str, message: str) -> None:
        if rule in self.allowed:
            return
        self.violations.append(Violation(self.rel, line, rule, message))

    def headings(self, level: int) -> list[tuple[int, str]]:
        found = []
        for i, line in enumerate(self.lines):
            if i in self.code_lines:
                continue
            match = HEADING_RE.match(line)
            if match and len(match.group("hashes")) == level:
                found.append((i + 1, match.group("text")))
        return found

    # -- rules --------------------------------------------------------------

    def check_h1(self) -> None:
        h1s = self.headings(1)
        if not h1s:
            self.add(1, "h1", "page has no H1 title")
        elif len(h1s) > 1:
            self.add(h1s[1][0], "h1", f"page has {len(h1s)} H1 headings, expected 1")
        for line, text in h1s:
            if text.endswith((".", ":", "!", "?")):
                self.add(line, "h1", f"H1 ends with punctuation: {text!r}")

    def check_heading_levels(self) -> None:
        previous = 0
        for i, line in enumerate(self.lines):
            if i in self.code_lines:
                continue
            match = HEADING_RE.match(line)
            if not match:
                continue
            level = len(match.group("hashes"))
            if previous and level > previous + 1:
                self.add(
                    i + 1,
                    "heading-skip",
                    f"heading level jumps from h{previous} to h{level}",
                )
            previous = level

    def check_section_vocabulary(self) -> None:
        for line, text in self.headings(2):
            for stem in CANONICAL_STEMS:
                if text.lower().startswith(stem.lower()):
                    if text not in CANONICAL_SECTIONS:
                        canonical = next(
                            (
                                s
                                for s in CANONICAL_SECTIONS
                                if s.lower().startswith(stem.lower())
                            ),
                            stem,
                        )
                        self.add(
                            line,
                            "heading-vocabulary",
                            f"{text!r} is a variant of the canonical section "
                            f"{canonical!r}; use the canonical wording verbatim",
                        )
                    break

    def check_heading_case(self) -> None:
        for level in (2, 3):
            for line, text in self.headings(level):
                if text in CANONICAL_SECTIONS or text in MODULE_SECTIONS:
                    continue
                words = re.findall(r"[A-Za-z][A-Za-z'’/-]*", text)
                for word in words[1:]:
                    if not word[0].isupper():
                        continue
                    if word.lower() in UI_PROPER_NOUNS or word.isupper():
                        continue
                    self.add(
                        line,
                        "heading-case",
                        f"h{level} {text!r} is not sentence case ({word!r})",
                    )
                    break

    def check_sections(self) -> None:
        present = [t for _, t in self.headings(2)]
        order = MODULE_SECTIONS if self.is_module_page else CANONICAL_SECTIONS
        mandatory = MODULE_MANDATORY if self.is_module_page else MANDATORY_SECTIONS

        for section in mandatory:
            if section not in present:
                self.add(1, "sections", f"missing mandatory section '## {section}'")

        indices = [(order.index(t), t) for t in present if t in order]
        for (a_idx, a_name), (b_idx, b_name) in zip(indices, indices[1:]):
            if b_idx < a_idx:
                line = next(ln for ln, t in self.headings(2) if t == b_name)
                self.add(
                    line,
                    "section-order",
                    f"'## {b_name}' appears after '## {a_name}'; "
                    f"canonical order is {' → '.join(order)}",
                )
                break

    def check_empty_sections(self) -> None:
        h2 = self.headings(2)
        for idx, (line, text) in enumerate(h2):
            end = h2[idx + 1][0] - 1 if idx + 1 < len(h2) else len(self.lines)
            body = [ln for ln in self.lines[line:end] if ln.strip()]
            if not body:
                self.add(line, "empty-section", f"section '## {text}' has no content")

    def check_admonitions(self) -> None:
        for i, line in enumerate(self.lines):
            if i in self.code_lines:
                continue
            match = ADMONITION_RE.match(line)
            if not match:
                continue
            type_token = match.group("type")
            if not match.group("space"):
                self.add(
                    i + 1,
                    "admonition",
                    f"missing space after '!!!' in {line.strip()!r}",
                )
            if type_token.lower() not in APPROVED_ADMONITIONS:
                self.add(
                    i + 1,
                    "admonition",
                    f"{type_token!r} is not an approved admonition type "
                    f"({', '.join(sorted(APPROVED_ADMONITIONS))}); "
                    f"a section title belongs in an H2, not an admonition",
                )
                continue
            if type_token != type_token.lower():
                self.add(
                    i + 1,
                    "admonition",
                    f"admonition type {type_token!r} must be lowercase",
                )
            rest = match.group("rest").strip()
            if rest and not re.fullmatch(r'"[^"]+"', rest):
                self.add(
                    i + 1,
                    "admonition",
                    f"admonition title must be double-quoted, found {rest!r}",
                )
            # Body must be indented, or the block renders as an empty box.
            base = len(match.group("indent"))
            j = i + 1
            while j < len(self.lines) and not self.lines[j].strip():
                j += 1
            if j >= len(self.lines):
                self.add(i + 1, "admonition", "admonition has no body")
                continue
            body = self.lines[j]
            if len(body) - len(body.lstrip()) < base + 4:
                self.add(
                    i + 1,
                    "admonition",
                    "admonition body is not indented 4 spaces; it will render "
                    "as an empty callout with loose text beneath it",
                )

    def check_terminology(self) -> None:
        for i, line in enumerate(self.lines):
            if i in self.code_lines or line.lstrip().startswith("<!--"):
                continue
            for pattern, replacement in FORBIDDEN_TERMS.items():
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    self.add(
                        i + 1,
                        "terminology",
                        f"{match.group(0)!r} is not approved; use {replacement!r} "
                        f"(STYLE_SPEC section 5)",
                    )
            for pattern, replacement in FORBIDDEN_MODULE_LABELS.items():
                match = re.search(pattern, line)
                if match:
                    self.add(
                        i + 1,
                        "module-label",
                        f"{match.group(0)!r} is not the nav label; use {replacement!r}",
                    )

    def check_prohibited_phrases(self) -> None:
        for i, line in enumerate(self.lines):
            if i in self.code_lines or line.lstrip().startswith("<!--"):
                continue
            for pattern, fix in PROHIBITED_PHRASES.items():
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    self.add(
                        i + 1,
                        "prohibited-phrase",
                        f"{match.group(0)!r} is prohibited; {fix} "
                        f"(STYLE_SPEC section 2)",
                    )

    def check_arrows(self) -> None:
        for i, line in enumerate(self.lines):
            if i in self.code_lines:
                continue
            if re.search(r"\*\*[^*]*->[^*]*\*\*|\w\s+->\s+\w", line):
                self.add(i + 1, "arrow", "use '→' rather than '->' in UI paths")

    def check_placeholders(self) -> None:
        for i, line in enumerate(self.lines):
            for needle in PLACEHOLDER_STRINGS:
                if needle in line:
                    self.add(
                        i + 1,
                        "placeholder",
                        f"unedited scaffolding text: {needle!r}",
                    )

    def check_horizontal_rules(self) -> None:
        h2 = self.headings(2)
        if len(h2) < 2:
            return
        for (start, _), (end, name) in zip(h2, h2[1:]):
            between = self.lines[start : end - 1]
            if not any(ln.strip() == HR for ln in between):
                self.add(
                    end,
                    "horizontal-rule",
                    f"missing 70-underscore divider before '## {name}' "
                    f"(STYLE_SPEC section 4.5)",
                )

    def check_tags(self) -> None:
        if not self.text.startswith("---\n"):
            self.add(1, "tags", "page has no frontmatter tags block")
            return
        end = self.text.find("\n---", 4)
        block = self.text[4:end] if end != -1 else ""
        match = re.search(r"^tags:\s*\[(.*?)\]", block, re.M | re.S)
        if not match:
            self.add(1, "tags", "frontmatter has no 'tags:' list")
            return
        tags = [t.strip() for t in match.group(1).split(",") if t.strip()]
        seen = set()
        for tag in tags:
            if ":" not in tag:
                self.add(1, "tags", f"tag {tag!r} must be '<namespace>:<value>'")
                continue
            namespace, value = tag.split(":", 1)
            if namespace not in TAG_NAMESPACES:
                self.add(
                    1,
                    "tags",
                    f"unknown tag namespace {namespace!r} "
                    f"(allowed: {', '.join(sorted(TAG_NAMESPACES))})",
                )
                continue
            if value not in TAG_VALUES[namespace]:
                self.add(
                    1,
                    "tags",
                    f"unknown value {value!r} for '{namespace}:' "
                    f"(allowed: {', '.join(sorted(TAG_VALUES[namespace]))})",
                )
            seen.add(namespace)
        if "module" not in seen:
            self.add(1, "tags", "page must carry a 'module:' tag")

    def run(self, rules: set[str] | None) -> list[Violation]:
        checks = {
            "h1": self.check_h1,
            "heading-skip": self.check_heading_levels,
            "heading-vocabulary": self.check_section_vocabulary,
            "heading-case": self.check_heading_case,
            "sections": self.check_sections,
            "empty-section": self.check_empty_sections,
            "admonition": self.check_admonitions,
            "terminology": self.check_terminology,
            "prohibited-phrase": self.check_prohibited_phrases,
            "arrow": self.check_arrows,
            "placeholder": self.check_placeholders,
            "horizontal-rule": self.check_horizontal_rules,
            "tags": self.check_tags,
        }
        for name, check in checks.items():
            if rules is None or name in rules:
                check()
        return self.violations


# ---------------------------------------------------------------------------


def collect(paths: list[Path], rules: set[str] | None) -> list[Violation]:
    violations: list[Violation] = []
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8")
        violations.extend(PageLinter(path, text).run(rules))
    return violations


def load_baseline() -> Counter[str]:
    if not BASELINE_PATH.exists():
        return Counter()
    data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return Counter(data.get("counts", {}))


def save_baseline(violations: list[Violation]) -> None:
    counts = Counter(v.key() for v in violations)
    BASELINE_PATH.write_text(
        json.dumps(
            {
                "_comment": (
                    "Known style violations, keyed by '<path>::<rule>'. Generated by "
                    "scripts/style_lint.py --update-baseline. Counts may only shrink; "
                    "any increase fails CI. The goal is an empty 'counts' object."
                ),
                "total": sum(counts.values()),
                "counts": dict(sorted(counts.items())),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def report_unverified(paths: list[Path]) -> int:
    """List every page carrying an explicit 'needs product review' marker."""
    by_module: dict[str, list[str]] = defaultdict(list)
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8")
        markers = []
        if "Needs product review" in text:
            markers.append("needs product review")
        todos = re.findall(r"<!--\s*TODO:\s*(.+?)\s*-->", text)
        markers.extend(todos)
        if markers:
            module = path.relative_to(DOCS_ROOT).parts[0]
            for marker in markers:
                by_module[module].append(f"{path.as_posix()} — {marker}")
    for module in sorted(by_module):
        print(f"\n## {module}")
        for entry in sorted(by_module[module]):
            print(f"- [ ] {entry}")
    total = sum(len(v) for v in by_module.values())
    print(f"\nTotal open items: {total}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--rules", help="comma-separated subset of rules to run")
    parser.add_argument("--no-baseline", action="store_true")
    parser.add_argument("--update-baseline", action="store_true")
    parser.add_argument("--stats", action="store_true", help="summarise by rule")
    parser.add_argument("--report-unverified", action="store_true")
    args = parser.parse_args()

    if args.paths:
        files = [p for p in args.paths if p.suffix == ".md" and p.is_file()]
    else:
        files = sorted(DOCS_ROOT.rglob("*.md"))
    if not files:
        return 0

    if args.report_unverified:
        return report_unverified(files)

    rules = {r.strip() for r in args.rules.split(",")} if args.rules else None
    violations = collect(files, rules)

    if args.update_baseline:
        save_baseline(violations)
        print(f"baseline updated: {len(violations)} violations recorded")
        return 0

    if args.stats:
        by_rule = Counter(v.rule for v in violations)
        width = max((len(r) for r in by_rule), default=10)
        for rule, count in by_rule.most_common():
            print(f"{count:>5}  {rule:<{width}}")
        print(f"{sum(by_rule.values()):>5}  TOTAL across {len(files)} files")
        return 0

    baseline = Counter() if args.no_baseline else load_baseline()
    current = Counter(v.key() for v in violations)

    new: list[Violation] = []
    quota = dict(baseline)
    for violation in violations:
        key = violation.key()
        if quota.get(key, 0) > 0:
            quota[key] -= 1
        else:
            new.append(violation)

    fixed = sum(max(0, baseline[k] - current.get(k, 0)) for k in baseline)

    if new:
        print(f"{len(new)} new style violation(s):\n", file=sys.stderr)
        for violation in new:
            print(f"  {violation}", file=sys.stderr)
        print(
            "\nFix these, or if a violation is a genuine exception add"
            "\n  <!-- style-lint: allow=<rule> -->\nto the page.",
            file=sys.stderr,
        )
        return 1

    remaining = sum(current.values())
    if remaining:
        message = f"style_lint: {remaining} known violation(s) remain in the baseline"
        if fixed:
            message += f" ({fixed} fixed since it was recorded — run --update-baseline)"
        print(message)
    else:
        print(f"style_lint: clean across {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
