#!/usr/bin/env python3
"""CTB2025 Docs utilities.

Subcommands:
  nav-sync   Create stub .md files for any nav entry that has no matching file.
  nav-audit  List nav entries missing files + files missing nav entries (no changes made).
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

DOCS_ROOT = Path("docs")
MKDOCS_CONFIG = Path("mkdocs.yml")
STUB_CONTENT = """# {title}
<!-- STUB: This page was auto-created by nav-sync. Fill in content using doc-writer. -->

## Summary

!!! warning "Under Construction"
    This page is under construction. Use `@doc-writer` or `make write-doc FILE={path}` to complete it.

## Related pages

- **[Dashboard](../00-getting-started/dashboard.md)** — Return to the main dashboard overview.
"""


# ---------------------------------------------------------------------------
# YAML loader that tolerates MkDocs custom tags such as !ENV
# yaml.safe_load raises ConstructorError on unknown tags; this loader ignores
# them and returns None so the nav structure is still fully parseable.
# ---------------------------------------------------------------------------
class _PermissiveLoader(yaml.SafeLoader):
    pass


def _ignore_unknown_tag(
    loader: yaml.SafeLoader, tag_suffix: str, node: yaml.Node
) -> None:  # noqa: ARG001
    return None


_PermissiveLoader.add_multi_constructor("", _ignore_unknown_tag)


def _load_nav_paths() -> list[str]:
    """Load and return all nav paths from mkdocs.yml, tolerating custom tags."""
    with open(MKDOCS_CONFIG) as f:
        config = yaml.load(f, Loader=_PermissiveLoader)  # noqa: S506 — permissive by design
    return _extract_nav_paths(config.get("nav", []))


# ---------------------------------------------------------------------------
# Nav path extraction
# ---------------------------------------------------------------------------
def _extract_nav_paths(nav: list, paths: list[str] | None = None) -> list[str]:
    """Recursively extract all .md file paths from a mkdocs nav structure."""
    if paths is None:
        paths = []
    for item in nav:
        if isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str) and value.endswith(".md"):
                    paths.append(value)
                elif isinstance(value, list):
                    _extract_nav_paths(value, paths)
        elif isinstance(item, str) and item.endswith(".md"):
            paths.append(item)
    return paths


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
def cmd_nav_sync() -> int:
    """Create stub .md files for any nav entry that has no matching file."""
    nav_paths = _load_nav_paths()
    created = 0
    for rel_path in nav_paths:
        target = DOCS_ROOT / rel_path
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        title = target.stem.replace("-", " ").replace("_", " ").title()
        content = STUB_CONTENT.format(title=title, path=str(target))
        target.write_text(content, encoding="utf-8")
        print(f"[nav-sync] Created stub: {target}")
        created += 1
    if created == 0:
        print("[nav-sync] All nav entries have matching files. Nothing to do.")
    else:
        print(f"[nav-sync] Done. {created} stub(s) created.")
    return 0


def cmd_nav_audit() -> int:
    """List nav entries missing files + files missing nav entries. No changes made."""
    nav_paths = set(_load_nav_paths())
    all_md = set(str(p.relative_to(DOCS_ROOT)) for p in DOCS_ROOT.rglob("*.md"))

    missing_files = sorted(p for p in nav_paths if not (DOCS_ROOT / p).exists())
    orphan_files = sorted(p for p in all_md if p not in nav_paths)

    if missing_files:
        print("\n❌ Nav entries with no matching file (run nav-sync to create stubs):")
        for p in missing_files:
            print(f"  - docs/{p}")
    else:
        print("\n✅ All nav entries have matching files.")

    if orphan_files:
        print("\n⚠️  Files not referenced in nav (consider adding or archiving):")
        for p in orphan_files:
            print(f"  - docs/{p}")
    else:
        print("✅ All .md files are referenced in nav.")

    return 0 if (not missing_files and not orphan_files) else 1


def _load_nav() -> list:
    with open(MKDOCS_CONFIG) as f:
        config = yaml.load(f, Loader=_PermissiveLoader)  # noqa: S506 — permissive by design
    return config.get("nav", [])


def _sidebar_lines(nav: list, depth: int = 0) -> list[str]:
    """Render a mkdocs nav tree as GitHub wiki sidebar Markdown.

    Top-level sections become H3 headings; anything nested inside them becomes
    an indented bullet list, so the wiki mirrors the site's hierarchy.
    """
    lines: list[str] = []
    indent = "  " * max(0, depth - 1)
    for item in nav:
        if isinstance(item, str) and item.endswith(".md"):
            lines.append(f"{indent}- [{_wiki_title(item)}]({_wiki_link(item)})")
        elif isinstance(item, dict):
            for label, value in item.items():
                if isinstance(value, str) and value.endswith(".md"):
                    lines.append(f"{indent}- [{label}]({_wiki_link(value)})")
                elif isinstance(value, list):
                    if depth == 0:
                        lines.extend(["", f"### {label}", ""])
                    else:
                        lines.append(f"{indent}- **{label}**")
                    lines.extend(_sidebar_lines(value, depth + 1))
    return lines


def _wiki_link(path: str) -> str:
    return path[: -len(".md")]


def _wiki_title(path: str) -> str:
    stem = Path(path).stem
    return "Module Overview" if stem == "README" else stem.replace("-", " ").title()


def cmd_sidebar_sync() -> int:
    """Regenerate docs/_Sidebar.md from the mkdocs nav.

    The wiki sidebar is published by wiki-sync.yml. Hand-maintaining it let it
    drift: it pointed at three renamed files, omitted a page, and omitted three
    whole modules. Generating it keeps the wiki and the site in step.
    """
    header = [
        "## CTB Admin Docs",
        "",
        "<!-- Generated by `python main.py sidebar-sync`. Do not edit by hand. -->",
        "",
    ]
    body = _sidebar_lines(_load_nav())
    text = "\n".join(header + body).replace("\n\n\n", "\n\n").strip() + "\n"
    target = DOCS_ROOT / "_Sidebar.md"
    changed = not target.exists() or target.read_text(encoding="utf-8") != text
    target.write_text(text, encoding="utf-8")
    print(f"[sidebar-sync] {'Updated' if changed else 'Already current:'} {target}")
    return 0


COMMANDS = {
    "nav-sync": cmd_nav_sync,
    "nav-audit": cmd_nav_audit,
    "sidebar-sync": cmd_sidebar_sync,
}


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Usage: python main.py <command>")
        print(f"Commands: {', '.join(COMMANDS)}")
        sys.exit(1)
    sys.exit(COMMANDS[sys.argv[1]]())


if __name__ == "__main__":
    main()
