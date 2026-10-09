#!/bin/bash
# Pre-commit: consistency kit + script compile. Mirrors .github/workflows/ci.yml.
#
# This repo has no venv, no requirements.txt and no pyproject.toml, so there is
# no dependency check to run — the kit itself is stdlib-only precisely so it can
# guard a repo that declares no environment.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Fail fast: a drifted version / count / routing surface is a content bug, and
# it is cheaper to see before the compile pass than after.
echo "Checking consistency kit..."
python3 "$ROOT/scripts/check_archviz.py"

echo "Checking consistency kit's own checker..."
python3 "$ROOT/scripts/check_archviz.py" --self-test >/dev/null

echo "Byte-compiling scripts..."
python3 -m compileall -q "$ROOT/scripts"
