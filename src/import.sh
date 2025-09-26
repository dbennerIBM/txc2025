#!/usr/bin/env bash
# import_all.sh
# Run all orchestrate imports for tools and agents

# Go to project directory
cd /mnt/c/Users/Sara/txc2025/src || exit 1

echo "=== Importing tools ==="
# Loop through all Python files in ./tools
for tool in ./tools/*.py; do
    echo "Importing tool: $tool"
    orchestrate tools import -k python -f "$tool"
done

echo
echo "=== Importing agents ==="
# Loop through all YAML files in ./agents
for agent in ./agents/*.yaml; do
    echo "Importing agent: $agent"
    orchestrate agents import -f "$agent"
done

echo
echo "=== Import completed ==="
