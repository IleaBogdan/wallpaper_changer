@echo off
REM Kill the running desktop_changer.exe process if it exists
taskkill /im desktop_changer.exe /f >nul 2>&1

REM Check if desktop_changer.exe exists and delete it
if exist desktop_changer.exe (
    del /f /q desktop_changer.exe
)

REM Compile main.py into desktop_changer.exe using pyinstaller (no console)
pyinstaller --onefile --noconsole --name desktop_changer main.py

REM Move the generated exe to the current directory (dist folder is default output)
move /Y dist\desktop_changer.exe .

REM Clean up build files
rmdir /s /q build
rmdir /s /q dist
del /q desktop_changer.spec

REM Start the WallpaperChanger task silently
schtasks /run /tn "WallpaperChanger" >nul 2>&1

echo Done!