# Start EduQuest API for local development (SQLite by default).
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..\backend

if (-not (Test-Path .\.venv\Scripts\python.exe)) {
  Write-Host "Creating venv with Python 3.11..."
  py -3.11 -m venv .venv
  .\.venv\Scripts\python -m pip install -U pip
  .\.venv\Scripts\python -m pip install -r requirements-dev.txt
}

Write-Host "Starting API on http://127.0.0.1:8000 ..."
Write-Host "Swagger: http://127.0.0.1:8000/docs"
.\.venv\Scripts\python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
