#!/usr/bin/env bash
set -euo pipefail

if git rev-parse --git-dir >/dev/null 2>&1; then
  {
    git log --since="midnight" --name-only --pretty=format:
    git diff --name-only
    git diff --staged --name-only
  } | sed '/^$/d' | sort -u
else
  echo "Not inside a git repository" >&2
  exit 1
fi
