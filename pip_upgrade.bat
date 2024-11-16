@echo off
set current_dir=%~dp0
"%current_dir%\Python-3.12.4\python.exe" -m pip install --upgrade pip
"%current_dir%\Python-3.12.4\python.exe" -m pip install pyinstaller
echo Only necessary packages have been installed.