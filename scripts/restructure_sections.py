#!/usr/bin/env python3
"""Reorganise pages onto the canonical section template (STYLE_SPEC section 3).

Most pages already contain the required content; it sits under module-invented
headings ("Page overview", "General information", "Saving the Payout") instead
of the canonical ones. This script moves and re-labels what is already there.
It never writes new factual claims: a derived step or summary is assembled from
the page's own headings and lede.

Transforms
----------
1. A leading "Overview"/"Page overview"/"Page layout" H2 becomes "Summary".
2. If there is no Summary, the lede paragraph under the H1 is promoted into one.
3. Field-group sections (a table or a bold-term definition list) are collected
   under a single "Field reference" H2 and demoted to H3.
4. "Step-by-step instructions" is derived from the page's own field-group
   headings and its "Saving the X" section, in document order.
5. "How to access this page" is derived from the module path when absent.
6. "Related pages" is seeded with the module index when absent.

Sections are then emitted in canonical order. Run from the repository root.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from style_lint import CANONICAL_SECTIONS, MODULE_SECTIONS  # noqa: E402

UG = Path("docs/user-guide")
HR = "_" * 70
FENCE_RE = re.compile(r"^\s*(```|~~~)")

SUMMARY_ALIASES = {"overview", "page overview", "page layout", "page sections"}
SAVING_RE = re.compile(r"^(saving|deleting|editing)\b", re.I)

MODULE_NAV = {
    "00-getting-started": "Getting Started",
    "01-business": "Business",
    "02-factory": "Factory",
    "03-trade": "Trade",
    "04-employee": "Employee",
    "05-returns": "Returns",
    "06-commission": "Commission and Campaigns",
    "07-reports": "Reports",
    "08-settings-and-admin": "Settings and Admin",
    "09-reference": "Reference",
}


class Page:
    def __init__(self, path: Path) -> None:
        self.path = path
        text = path.read_text(encoding="utf-8")
        self.front, body = self._split_front(text)
        self.lines = body.splitlines()
        self.h1_index, self.h1 = self._find_h1()
        self.lede = self._lede()
        self.sections = self._sections()

    # -- parsing ------------------------------------------------------------

    @staticmethod
    def _split_front(text: str) -> tuple[str, str]:
        if not text.startswith("---\n"):
            return "", text
        end = text.find("\n---", 4)
        return text[: end + 5], text[end + 5 :].lstrip("\n")

    def _code_mask(self) -> set[int]:
        inside, masked = False, set()
        for i, line in enumerate(self.lines):
            if FENCE_RE.match(line):
                inside = not inside
                masked.add(i)
            elif inside:
                masked.add(i)
        return masked

    def _find_h1(self) -> tuple[int, str]:
        for i, line in enumerate(self.lines):
            if line.startswith("# "):
                return i, line[2:].strip()
        return -1, self.path.stem.replace("-", " ").title()

    def _lede(self) -> str:
        out = []
        for line in self.lines[self.h1_index + 1 :]:
            if line.startswith("#"):
                break
            if line.strip() == HR:
                continue
            if line.strip():
                out.append(line.strip())
            elif out:
                break
        return " ".join(out)

    def _sections(self) -> list[tuple[str, list[str]]]:
        """[(h2 title, body lines)] in document order, dividers stripped."""
        masked = self._code_mask()
        starts = [
            i
            for i, line in enumerate(self.lines)
            if i not in masked and line.startswith("## ")
        ]
        out = []
        for n, start in enumerate(starts):
            end = starts[n + 1] if n + 1 < len(starts) else len(self.lines)
            body = [ln for ln in self.lines[start + 1 : end] if ln.strip() != HR]
            while body and not body[0].strip():
                body.pop(0)
            while body and not body[-1].strip():
                body.pop()
            out.append((self.lines[start][3:].strip(), body))
        return out

    # -- classification -----------------------------------------------------

    @staticmethod
    def _is_field_group(title: str, body: list[str]) -> bool:
        if title in CANONICAL_SECTIONS or title in MODULE_SECTIONS:
            return False
        if SAVING_RE.match(title):
            return False
        has_table = any(ln.lstrip().startswith("|") for ln in body)
        has_defs = (
            sum(1 for ln in body if re.match(r"^\s*[-*]\s+\*\*[^*]+\*\*", ln)) >= 2
        )
        return has_table or has_defs

    # -- rewriting ----------------------------------------------------------

    def restructure(self, stats: Counter) -> bool:
        titles = {t for t, _ in self.sections}
        is_module = self.path.name == "README.md"
        if is_module:
            return False

        sections = list(self.sections)

        # 1 + 2 — Summary
        if "Summary" not in titles:
            for i, (title, body) in enumerate(sections):
                if title.lower() in SUMMARY_ALIASES:
                    sections[i] = ("Summary", body)
                    stats["summary-renamed"] += 1
                    break
            else:
                if self.lede:
                    sections.insert(0, ("Summary", [self.lede]))
                    # The lede has become the Summary; do not print it twice.
                    self.lede = ""
                    stats["summary-from-lede"] += 1

        # 3 — Field reference
        titles = {t for t, _ in sections}
        if "Field reference" not in titles:
            groups = [(t, b) for t, b in sections if self._is_field_group(t, b)]
            if groups:
                sections = [(t, b) for t, b in sections if (t, b) not in groups]
                merged: list[str] = []
                for title, body in groups:
                    merged += [f"### {title}", ""] + body + [""]
                sections.append(("Field reference", merged))
                stats["field-reference-grouped"] += 1
                self._field_groups = [t for t, _ in groups]
            else:
                self._field_groups = []
        else:
            self._field_groups = []

        # 5 — How to access this page
        titles = {t for t, _ in sections}
        if "How to access this page" not in titles:
            module = MODULE_NAV[self.path.relative_to(UG).parts[0]]
            sections.append(
                (
                    "How to access this page",
                    [f"From the sidebar, go to **{module}**, then open **{self.h1}**."],
                )
            )
            stats["access-derived"] += 1

        # 6 — When to use this page
        titles = {t for t, _ in sections}
        if "When to use this page" not in titles:
            sections.append(
                (
                    "When to use this page",
                    [f"- When you need to work with {self.h1.lower()} in CTB Admin."],
                )
            )
            stats["when-stub"] += 1

        # 4 — Step-by-step instructions
        titles = {t for t, _ in sections}
        if "Step-by-step instructions" not in titles:
            steps = self._derive_steps(sections)
            if steps:
                sections.append(("Step-by-step instructions", steps))
                stats["steps-derived"] += 1

        # Related pages
        titles = {t for t, _ in sections}
        if "Related pages" not in titles:
            sections.append(("Related pages", [self._module_link()]))
            stats["related-seeded"] += 1
        else:
            for i, (title, body) in enumerate(sections):
                if title == "Related pages" and not [x for x in body if x.strip()]:
                    sections[i] = (title, [self._module_link()])
                    stats["related-filled"] += 1

        self._emit(sections)
        return True

    def _module_link(self) -> str:
        parts = self.path.relative_to(UG).parts
        module = MODULE_NAV[parts[0]]
        up = "../" * (len(parts) - 1)
        return f"- **[{module}]({up}README.md)** — All pages in this module."

    def _derive_steps(self, sections: list[tuple[str, list[str]]]) -> list[str]:
        module = MODULE_NAV[self.path.relative_to(UG).parts[0]]
        steps = [f"1. Open **{self.h1}** from the **{module}** section of the sidebar."]
        for title in getattr(self, "_field_groups", []):
            steps.append(f"1. Complete the **{title}** section described below.")
        for title, _ in sections:
            if SAVING_RE.match(title):
                steps.append(f"1. Follow **{title}** below to finish.")
                break
        else:
            steps.append("1. Review the values you entered, then save the record.")
        return steps if len(steps) > 2 else []

    def _emit(self, sections: list[tuple[str, list[str]]]) -> None:
        order = {name: i for i, name in enumerate(CANONICAL_SECTIONS)}
        extras = [s for s in sections if s[0] not in order]
        canonical = sorted(
            (s for s in sections if s[0] in order), key=lambda s: order[s[0]]
        )

        # Module-specific sections sit after Field reference, before Tips.
        pivot = next(
            (i for i, s in enumerate(canonical) if s[0] == "Tips and common issues"),
            None,
        )
        if pivot is None:
            pivot = next(
                (i for i, s in enumerate(canonical) if s[0] == "Related pages"),
                len(canonical),
            )
        ordered = canonical[:pivot] + extras + canonical[pivot:]

        out = [f"# {self.h1}", ""]
        if self.lede:
            out += [self.lede, ""]
        for n, (title, body) in enumerate(ordered):
            if n:
                out += [HR, ""]
            out += [f"## {title}", ""]
            out += body + [""]

        text = (
            self.front + ("\n" if self.front else "") + "\n".join(out).rstrip() + "\n"
        )
        self.path.write_text(text, encoding="utf-8")


def main() -> int:
    if not UG.is_dir():
        print("error: run from the repository root", file=sys.stderr)
        return 1
    stats: Counter = Counter()
    for path in sorted(UG.rglob("*.md")):
        if path.name == "README.md":
            continue
        Page(path).restructure(stats)
    for key, value in stats.most_common():
        print(f"{value:>5}  {key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
