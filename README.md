# Wallpaper Changer

A lightweight Python script for Windows that automatically switches your desktop wallpaper when the desktop is not visible (e.g., when a window is in focus).

---

## Setup Instructions

1. **Download or Clone the Repository**  
   - Either download the ZIP file or run:  
     ```bash
     git clone https://github.com/IleaBogdan/wallpaper_changer.git
     ```

2. **Build the Executable**  
   - In Command Prompt, navigate to the project folder and run:  
     ```cmd
     build.bat
     ```

3. **Configure in Task Scheduler**  
   - Open **Task Scheduler**  
   - Click **Create Task** (not *Create Basic Task*)  
   - In the **General** tab:
     - Name it: `WallpaperChanger`
     - Check **Run with highest privileges**
   - Go to the **Triggers** tab:
     - Click **New**
     - Set *Begin the task* to **At log on**
     - Click **OK**
   - Go to the **Actions** tab:
     - Click **New**
     - Set *Action* to **Start a program**
     - In *Program/script*, browse and select the `.exe` file from the project folder
     - **Important**: Set *Start in* to the folder where the `.exe` is located
     - Click **OK**
   - Click **OK** to save the task

---

## Customization

- Replace the images in the `wallpapers/` folder:
  - `wp1.jpg` – shown when the desktop is **visible**
  - `wp2.jpg` – shown when the desktop is **not visible**
- You can update the images at any time — **no need to rebuild the executable** after replacing them.
