@echo off
:: 設置當前目錄
set current_dir=%~dp0

:: 設置7za.exe的路徑
set seven_zip_exe=%current_dir%7-Zip Extra\7za.exe

:: 設置要壓縮的目標文件夾
set target_dir=%current_dir%python-3.12.4

:: 設置壓縮文件的輸出路徑
set output_zip=%current_dir%python-3.12.4.7z

:: 使用 7za.exe 壓縮文件夾，設置壓縮級別為最高，使用LZMA2方法
"%seven_zip_exe%" a -t7z -mx=9 -m0=lzma2 "%output_zip%" "%target_dir%"

:: 暫停腳本以便查看輸出結果
pause
