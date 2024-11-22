@echo off
set current_dir=%~dp0
set python_dir=%current_dir%
set seven_zip_dir=%current_dir%7-Zip Extra

if not exist "%python_dir%python-3.12.4" (
    "%seven_zip_dir%\7za.exe" x "%current_dir%python-3.12.4.7z" -o"%python_dir%"
)

set "python_exe=%python_dir%\python-3.12.4\python.exe"

call "%current_dir%pip_upgrade.bat"

powershell -Command "Start-Process '%python_exe%' -ArgumentList '\"%current_dir%/scripts/main.py\"' -Verb runAs"