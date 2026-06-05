# Creates a local virtual environment and installs pygame for PyCharm / terminal use.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$python = $null
foreach ($cmd in @("py -3", "python", "python3")) {
    try {
        $version = Invoke-Expression "$cmd --version" 2>$null
        if ($LASTEXITCODE -eq 0 -or $version) {
            $python = $cmd
            break
        }
    } catch {}
}

if (-not $python) {
    Write-Host "Python not found. Install from https://www.python.org/downloads/ then run this script again."
    exit 1
}

if (-not (Test-Path ".venv")) {
    Write-Host "Creating .venv ..."
    Invoke-Expression "$python -m venv .venv"
}

Write-Host "Installing dependencies ..."
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\pip.exe" install -r requirements.txt

Write-Host ""
Write-Host "Done. In PyCharm:"
Write-Host "  1. File -> Open -> select this folder"
Write-Host "  2. Settings -> Project -> Python Interpreter -> Add -> Existing -> .venv\Scripts\python.exe"
Write-Host "  3. Run the 'Drawing App' configuration (green play button)"
