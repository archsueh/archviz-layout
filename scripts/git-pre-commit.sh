#!/bin/bash
# Pre-commit: consistency kit + script compile. Mirrors .github/workflows/ci.yml.
#
# No venv check here: the kit is stdlib-only on purpose, so it can guard this
# repo from a bare Python. The dependency install step lives in CI only —
# running it on every commit would make committing depend on the network.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Fail fast: a drifted version / count / routing surface / unreachable reference
# / undeclared import is a content bug, and it is cheaper to see before the
# compile pass than after.
echo "Checking consistency kit..."
python3 "$ROOT/scripts/check_archviz.py"

echo "Checking consistency kit's own checker..."
python3 "$ROOT/scripts/check_archviz.py" --self-test >/dev/null

echo "Byte-compiling scripts..."
python3 -m compileall -q "$ROOT/scripts"
