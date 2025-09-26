# import_all.ps1
# Navigate to the project root
Set-Location "C:\Users\Sara\txc2025\src"

Write-Host "=== Importing tools ==="
# Loop through all Python files in ./tools
Get-ChildItem -Path "./tools" -Filter *.py | ForEach-Object {
    $toolPath = $_.FullName
    Write-Host "Importing tool: $toolPath"
    orchestrate tools import -k python -f $toolPath
}

Write-Host "`n=== Importing agents ==="
# Loop through all YAML files in ./agents
Get-ChildItem -Path "./agents" -Filter *.yaml | ForEach-Object {
    $agentPath = $_.FullName
    Write-Host "Importing agent: $agentPath"
    orchestrate agents import -f $agentPath
}

Write-Host "`n=== Import completed ==="
