$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
Push-Location -LiteralPath $projectRoot
try {
    if (-not (Test-Path -LiteralPath 'node_modules/@tailwindcss/cli/package.json')) {
        & npm.cmd ci --fetch-retries=0 --fetch-timeout=30000
        if ($LASTEXITCODE -ne 0) { throw 'Installing the locked asset dependencies failed.' }
    }
    & npm.cmd run build
    if ($LASTEXITCODE -ne 0) { throw 'Asset compilation failed.' }
} finally { Pop-Location }
