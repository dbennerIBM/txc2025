#!/usr/bin/env bash
# import_all.sh
# Runs orchestrate imports for tools and agents

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Go to project root
cd "$SCRIPT_DIR" || exit 1

echo "=== Importing tools ==="
for tool in ./tools/*.py; do
    echo "Importing tool: $tool"
    orchestrate tools import -k python -f "$tool"
done

echo
echo "=== Importing agents ==="
for agent in ./agents/*.yaml; do
    echo "Importing agent: $agent"
    orchestrate agents import -f "$agent"
done

echo
echo "=== Import completed ==="
