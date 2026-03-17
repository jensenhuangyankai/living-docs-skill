#!/usr/bin/env python3
from __future__ import annotations

import fnmatch
import sys
from pathlib import Path


def extract_globs(doc_path: Path) -> list[str]:
    lines = doc_path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return []

    globs: list[str] = []
    in_source_files = False

    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("source_files:"):
            in_source_files = True
            continue
        if in_source_files:
            if line and not line.startswith((" ", "\t")):
                in_source_files = False
                continue
            stripped = line.strip()
            if stripped.startswith("- "):
                globs.append(stripped[2:].strip())

    return globs


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: match-source-files.py <changed-file> [...]", file=sys.stderr)
        return 1

    docs_root = Path("docs")
    if not docs_root.exists():
        print("docs directory not found", file=sys.stderr)
        return 1

    changed_files = sys.argv[1:]
    matched: list[str] = []

    for doc_path in docs_root.rglob("*.md"):
        globs = extract_globs(doc_path)
        if any(fnmatch.fnmatch(changed, pattern) for pattern in globs for changed in changed_files):
            matched.append(str(doc_path))

    for path in sorted(set(matched)):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
