@echo off
REM Kill the running desktop_changer.exe process if it exists
taskkill /im desktop_changer.exe /f >nul 2>&1

REM Wait a bit to ensure the process is stopped
timeout /t 2 >nul

REM Check if desktop_changer.exe exists and delete it
if exist desktop_changer.exe (
    del /f /q desktop_changer.exe
    REM Wait to ensure file is unlocked
    timeout /t 1 >nul
)

REM Compile main.py into desktop_changer.exe using pyinstaller (no console)
pyinstaller --onefile --noconsole --name desktop_changer main.py

REM Move the generated exe to the current directory (dist folder is default output)
move /Y dist\desktop_changer.exe .

REM Clean up build files
rmdir /s /q build
rmdir /s /q dist
del /q desktop_changer.spec

REM Check if the WallpaperChanger task exists
schtasks /query /tn "WallpaperChanger" >nul 2>&1
if %errorlevel%==0 (
    schtasks /run /tn "WallpaperChanger" >nul 2>&1
    echo Updated task sch.
) else (
    echo Need to set-up task sch.
)

echo Done!