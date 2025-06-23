# wallpaper_changer
A Python script for Windows that sets a different wallpaper when the desktop is not visible.

---
## Set-up
 - Download the zip or clone the repo.
 - Run build.bat in cmd in the project folder.
 - Open Task Scheduler.
 - Click `Create Task` (not `Create Basic Task`)
 - Give it the name WallpaperChanger.
 - Go to `Triggers` tab. Click `New` and set "Begin the task" `At log on`. CLick `Ok`.
 - Go to `Actions` tab. Click `New` and set "Action" to Start a program.
 - In `Program/script` browse and add the .exe from the project folder.
 - !!! Set the `Start in` to be the folder where you will have the .exe in. Click `Ok`.
 - In `General` tab set `Run with highest privileges` and the click `Ok`.

## Customization
You can change the wallpapers in *wallpapers* folder.     
Just make sure they have the name `wp1.jpg` for the one to be displayed when watching the screen and `wp2.jpg` for the other one.      
You don't need to rerun the build file after updating the pictures.
