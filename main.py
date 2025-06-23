import os
import time
import ctypes
import win32api
import win32con
import win32gui
import psutil
from pathlib import Path

# Log the start directory
with open("C:\\Work\\wallpaper_changer\\log.txt", "a") as f:
    f.write(f"Started in: {os.getcwd()}\n")

# wp == wallpaper
wp_dir=Path("./wallpapers")
# wpn == wallpaper_name
active_wpn="wp1.jpg" 
idle_wpn="wp2.jpg"
# the time befor the image changes
IDLE_TIME=2

def set_wallpaper(image_path):
    image_path = Path(image_path).resolve()  # Ensure absolute path
    if not image_path.exists():  # checking if image is there
        print(f"Error: Wallpaper not found at {image_path}")
        return
    # setting the image as wallpaper
    ctypes.windll.user32.SystemParametersInfoW(
        win32con.SPI_SETDESKWALLPAPER, 0, str(image_path), win32con.SPIF_UPDATEINIFILE
    )

def get_idle_time():
    last_input=win32api.GetLastInputInfo()
    current_time=win32api.GetTickCount()
    return (current_time-last_input)/1000 # converting to seconds

def is_user_active():
    return get_idle_time()<IDLE_TIME # checking if the idle time is bigger then the const IDLE_TIME 

def get_active_window_process():
    window=win32gui.GetForegroundWindow()
    pid=win32process.GetWindowThreadProcessId(window)[1]
    return psutil.Process(pid).name()

def is_desktop_focused():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == 0:
        return False
    class_name = win32gui.GetClassName(hwnd)
    return class_name in ("Progman", "WorkerW")

def is_foreground_fullscreen():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == 0:
        return False
    rect = win32gui.GetWindowRect(hwnd)
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    return rect == (0, 0, screen_width, screen_height)

def is_foreground_maximized():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == 0:
        return False
    placement = win32gui.GetWindowPlacement(hwnd)
    return placement[1] == win32con.SW_SHOWMAXIMIZED

def main():
    wp_dir.mkdir(exist_ok=True)
    active_wpn_path = wp_dir / active_wpn
    idle_wpn_path = wp_dir / idle_wpn

    last_wallpaper = None

    while True:
        if is_foreground_fullscreen() or is_foreground_maximized():
            if last_wallpaper != "idle":
                set_wallpaper(idle_wpn_path)
                last_wallpaper = "idle"
        else:
            if last_wallpaper != "active":
                set_wallpaper(active_wpn_path)
                last_wallpaper = "active"
        time.sleep(1)

if __name__ == "__main__":
    import win32process
    try:
        main()
    except KeyboardInterrupt:
        print("Wallpaper changer stopped by user.")