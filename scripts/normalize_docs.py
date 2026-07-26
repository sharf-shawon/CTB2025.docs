#!/usr/bin/env python3
"""Apply the mechanical parts of the style spec across the user guide.

Deterministic transforms only — anything needing editorial judgement is left
for a human. Run from the repository root. Idempotent.

Covers:
  * canonical H2 wording (parameterised variants -> the fixed spec string)
  * sentence case for headings, preserving UI labels and acronyms
  * nav labels ("Trade Management" -> "Trade")
  * arrow style in UI paths
  * approved terminology
  * 70-underscore dividers between H2 sections
  * tag frontmatter derived from the page's path and filename
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from style_lint import (  # noqa: E402
    CANONICAL_SECTIONS,
    CANONICAL_STEMS,
    UI_PROPER_NOUNS,
)

UG = Path("docs/user-guide")
HR = "_" * 70

HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")

MODULE_LABELS = {
    "Trade Management": "Trade",
    "Employee Management": "Employee",
    "Business Management": "Business",
    "Factory Management": "Factory",
    "Settings Management": "Settings and Admin",
}

# Case-preserving terminology corrections (STYLE_SPEC section 5).
TERMS = [
    (r"\bCustomers\b", "Clients"),
    (r"\bCustomer\b", "Client"),
    (r"\bcustomers\b", "clients"),
    (r"\bcustomer\b", "client"),
    (r"\bSuppliers\b", "Vendors"),
    (r"\bSupplier\b", "Vendor"),
    (r"\bsuppliers\b", "vendors"),
    (r"\bsupplier\b", "vendor"),
    (r"\bDisbursements\b", "Payouts"),
    (r"\bDisbursement\b", "Payout"),
    (r"\bdisbursements\b", "payouts"),
    (r"\bdisbursement\b", "payout"),
    (r"\bleft menu\b", "sidebar"),
    (r"\bnavigation panel\b", "sidebar"),
    (r"\bhome screen\b", "Dashboard"),
]

MODULE_TAGS = {
    "00-getting-started": ("getting-started", "staff"),
    "01-business": ("business", "staff"),
    "02-factory": ("factory", "staff"),
    "03-trade": ("trade", "accountant"),
    "04-employee": ("employee", "hr"),
    "05-returns": ("returns", "staff"),
    "06-commission": ("commission", "accountant"),
    "07-reports": ("reports", "accountant"),
    "08-settings-and-admin": ("settings", "admin"),
    "09-reference": ("reference", "staff"),
}


def code_mask(lines: list[str]) -> set[int]:
    inside, masked = False, set()
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            inside = not inside
            masked.add(i)
        elif inside:
            masked.add(i)
    return masked


def sentence_case(text: str) -> str:
    """Lowercase mid-heading words unless they are UI labels or acronyms."""
    tokens = re.split(r"(\W+)", text)
    out, seen_word = [], False
    for token in tokens:
        if not token or not token[0].isalpha():
            out.append(token)
            continue
        if not seen_word:
            seen_word = True
            out.append(token)
            continue
        if token.isupper() or token.lower() in UI_PROPER_NOUNS:
            out.append(token)
        elif token[0].isupper():
            out.append(token[0].lower() + token[1:])
        else:
            out.append(token)
    return "".join(out)


def canonicalise_heading(text: str) -> str:
    for stem in CANONICAL_STEMS:
        if text.lower().startswith(stem.lower()):
            for section in CANONICAL_SECTIONS:
                if section.lower().startswith(stem.lower()):
                    return section
    return text


def derive_tags(path: Path) -> str:
    parts = path.relative_to(UG).parts
    if len(parts) == 1:  # docs/user-guide/README.md — the Start Here page
        return "[module:getting-started, task:view, role:staff]"
    module, role = MODULE_TAGS[parts[0]]
    stem = path.stem
    if stem.startswith(("add-", "create-")):
        task = "create"
    elif stem.startswith(("edit-", "manage-", "record-", "generate-")):
        task = "edit"
    elif (
        stem.endswith(("-report", "-reports"))
        or "report" in stem
        or "analytics" in stem
    ):
        task = "report"
    elif module == "settings" or stem in {
        "app-settings",
        "maintenance-mode",
        "sms-notifications",
    }:
        task = "configure"
    elif stem in {"troubleshooting", "error-pages", "offline-mode"}:
        task = "troubleshoot"
    else:
        task = "view"
    return f"[module:{module}, task:{task}, role:{role}]"


def process(path: Path, stats: Counter) -> None:
    original = path.read_text(encoding="utf-8")
    text = original

    # -- frontmatter tags ---------------------------------------------------
    if not text.startswith("---\n"):
        text = f"---\ntags: {derive_tags(path)}\n---\n\n{text}"
        stats["tags"] += 1

    lines = text.splitlines()
    masked = code_mask(lines)

    # -- headings -----------------------------------------------------------
    for i, line in enumerate(lines):
        if i in masked:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        hashes, body = match.group(1), match.group(2)
        new = canonicalise_heading(body) if len(hashes) == 2 else body
        if new != body:
            stats["heading-vocabulary"] += 1
        if new not in CANONICAL_SECTIONS:
            cased = sentence_case(new)
            if cased != new:
                stats["heading-case"] += 1
            new = cased
        if new != body:
            lines[i] = f"{hashes} {new}"

    # -- inline text --------------------------------------------------------
    for i, line in enumerate(lines):
        if i in masked or line.lstrip().startswith("<!--"):
            continue
        updated = line
        for old, new in MODULE_LABELS.items():
            if old in updated:
                updated = updated.replace(old, new)
                stats["module-label"] += 1
        for pattern, replacement in TERMS:
            updated, n = re.subn(pattern, replacement, updated)
            stats["terminology"] += n
        swapped = re.sub(r"(?<=\S) -> (?=\S)", " → ", updated)
        if swapped != updated:
            stats["arrow"] += 1
        lines[i] = swapped

    # -- 70-underscore dividers between H2 sections -------------------------
    masked = code_mask(lines)
    out: list[str] = []
    for i, line in enumerate(lines):
        if i not in masked and HEADING_RE.match(line) and line.startswith("## "):
            body = [ln for ln in out if ln.strip()]
            if body and not body[-1].strip() == HR and body[-1].lstrip()[:1] != "#":
                while out and not out[-1].strip():
                    out.pop()
                out.extend(["", HR, ""])
                stats["horizontal-rule"] += 1
        out.append(line)

    text = "\n".join(out).rstrip() + "\n"
    if text != original:
        path.write_text(text, encoding="utf-8")
        stats["files"] += 1


def main() -> int:
    if not UG.is_dir():
        print("error: run from the repository root", file=sys.stderr)
        return 1
    stats: Counter = Counter()
    for path in sorted(UG.rglob("*.md")):
        process(path, stats)
    width = max(len(k) for k in stats)
    for key, value in stats.most_common():
        print(f"{value:>5}  {key:<{width}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
