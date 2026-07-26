#!/usr/bin/env python3
"""One-shot repair for malformed MkDocs Material admonitions.

Three defects are fixed, all of which change how a page renders:

1. Body text is not indented under the ``!!!`` marker. Python-Markdown then
   closes the admonition immediately, so the page shows an empty coloured box
   followed by loose, unstyled body text.
2. ``!!! Tips and common issues`` uses the section title as the admonition
   *type*, emitting ``class="admonition tips and common issues"`` — a class the
   theme has no rules for — and replacing the mandatory H2 section, which
   removes the content from the page table of contents.
3. Where a tips block was indented and later reformatted by ``mdformat``, the
   body was rewritten as an indented code block, so the tips render as literal
   code.

Run from the repository root. Idempotent.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS_ROOT = Path("docs/user-guide")

APPROVED_TYPES = {"info", "tip", "warning", "note"}
TIPS_HEADING = "## Tips and common issues"

ADMONITION_RE = re.compile(r"^!!!\s*(?P<type>\S+)(?P<rest>.*)$")
BOUNDARY_RE = re.compile(r"^(#{1,6}\s|_{10,}\s*$|!!!|```)")


def _is_tips_marker(type_token: str, rest: str) -> bool:
    """True when the admonition abuses the Tips section title as its type."""
    return f"{type_token}{rest}".strip().lower().startswith("tips")


def _body_extent(lines: list[str], start: int) -> tuple[int, int]:
    """Return (body_start, body_end) for the block opened at ``start``.

    The body is the contiguous run of non-blank lines following the marker,
    after skipping blank lines. Deliberately conservative: a paragraph break
    ends the body, so unrelated prose is never pulled into a callout.
    """
    i = start + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or BOUNDARY_RE.match(lines[i]):
        return i, i
    body_start = i
    while i < len(lines) and lines[i].strip() and not BOUNDARY_RE.match(lines[i]):
        i += 1
    return body_start, i


def _fenced_body_extent(lines: list[str], start: int) -> tuple[int, int] | None:
    """Return (open_fence, close_fence) when the block's body became a code fence."""
    i = start + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or not lines[i].startswith("```"):
        return None
    j = i + 1
    while j < len(lines) and not lines[j].startswith("```"):
        j += 1
    if j >= len(lines):
        return None
    return i, j


def _dedent(line: str) -> str:
    if line.startswith("    "):
        return line[4:]
    return line.lstrip() if line.startswith("\t") else line


def convert_file(path: Path) -> dict[str, int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    stats = {"indented": 0, "tips_to_heading": 0, "unfenced": 0, "type_normalised": 0}
    out: list[str] = []
    i = 0

    while i < len(lines):
        match = ADMONITION_RE.match(lines[i])
        if not match:
            out.append(lines[i])
            i += 1
            continue

        type_token, rest = match.group("type"), match.group("rest")

        if _is_tips_marker(type_token, rest):
            fenced = _fenced_body_extent(lines, i)
            if fenced:
                open_fence, close_fence = fenced
                out.append(TIPS_HEADING)
                out.append("")
                out.extend(_dedent(line) for line in lines[open_fence + 1 : close_fence])
                stats["tips_to_heading"] += 1
                stats["unfenced"] += 1
                i = close_fence + 1
            else:
                body_start, body_end = _body_extent(lines, i)
                out.append(TIPS_HEADING)
                out.append("")
                out.extend(_dedent(line) for line in lines[body_start:body_end])
                stats["tips_to_heading"] += 1
                i = body_end
            continue

        canonical = type_token.lower()
        if canonical not in APPROVED_TYPES:
            out.append(lines[i])
            i += 1
            continue
        if canonical != type_token:
            stats["type_normalised"] += 1

        marker = f"!!! {canonical}{rest}".rstrip()
        body_start, body_end = _body_extent(lines, i)
        if body_start == body_end:
            out.append(marker)
            i += 1
            continue

        needs_indent = any(
            not lines[n].startswith(("    ", "\t")) for n in range(body_start, body_end)
        )
        out.append(marker)
        if needs_indent:
            out.extend(f"    {line.strip()}" for line in lines[body_start:body_end])
            stats["indented"] += 1
        else:
            out.extend(lines[body_start:body_end])
        i = body_end

    text = "\n".join(out).rstrip() + "\n"
    if text != path.read_text(encoding="utf-8"):
        path.write_text(text, encoding="utf-8")
    return stats


def main() -> int:
    if not DOCS_ROOT.is_dir():
        print(f"error: run from the repository root ({DOCS_ROOT} not found)", file=sys.stderr)
        return 1

    totals = {"indented": 0, "tips_to_heading": 0, "unfenced": 0, "type_normalised": 0}
    touched = 0
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        stats = convert_file(path)
        if any(stats.values()):
            touched += 1
        for key, value in stats.items():
            totals[key] += value

    print(f"files touched:            {touched}")
    print(f"bodies indented:          {totals['indented']}")
    print(f"tips blocks -> H2:        {totals['tips_to_heading']}")
    print(f"  of which un-fenced:     {totals['unfenced']}")
    print(f"admonition types fixed:   {totals['type_normalised']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
