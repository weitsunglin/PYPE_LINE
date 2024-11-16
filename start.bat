@echo off
set current_dir=%~dp0
set python_dir=%current_dir%
set seven_zip_dir=%current_dir%7-Zip Extra

if not exist "%python_dir%python-3.12.4" (
    echo Python-3.12.4 directory does not exist, extracting...
    "%seven_zip_dir%\7za.exe" x "%current_dir%python-3.12.4.7z" -o"%python_dir%"
    if errorlevel 1 (
        echo Extraction failed.
        pause
        exit /b 1
    )
    echo Extraction completed.
)

set "python_exe=%python_dir%\python-3.12.4\python.exe"
call "%current_dir%pip_upgrade.bat"

if exist "%python_exe%" (
    "%python_exe%" "%current_dir%/scripts/main.py"
) else (
    echo Python executable not found at "%python_exe%".
)