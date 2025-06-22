@echo off
REM Kill any running main.exe
taskkill /f /im main.exe >nul 2>&1

REM Compile main.py to an executable
pyinstaller --onefile --windowed main.py

REM Check if the build was successful
IF EXIST dist\main.exe (
    echo Running main.exe...
    dist\main.exe
) ELSE (
    echo Build failed. main.exe not found.
)