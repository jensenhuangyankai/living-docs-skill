#!/usr/bin/env bash
set -euo pipefail

repo_root="${1:-.}"
docs_dir="${repo_root%/}/docs"

mkdir -p \
  "$docs_dir/architecture" \
  "$docs_dir/services" \
  "$docs_dir/features" \
  "$docs_dir/ui"

touch \
  "$docs_dir/DESIGN.md" \
  "$docs_dir/CHANGELOG.md"

printf 'Scaffolded %s\n' "$docs_dir"
