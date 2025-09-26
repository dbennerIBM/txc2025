# import_all.ps1
# Runs orchestrate imports for tools and agents

# Get the folder where this script lives
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Change to the project root (same folder as this script)
Set-Location $ScriptDir

Write-Host "=== Importing tools ==="
Get-ChildItem -Path "./tools" -Filter *.py | ForEach-Object {
    Write-Host "Importing tool: $($_.Name)"
    orchestrate tools import -k python -f $_.FullName
}

Write-Host "`n=== Importing agents ==="
Get-ChildItem -Path "./agents" -Filter *.yaml | ForEach-Object {
    Write-Host "Importing agent: $($_.Name)"
    orchestrate agents import -f $_.FullName
}

Write-Host "`n=== Import completed ==="
