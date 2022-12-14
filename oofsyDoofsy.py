import os, shutil, time, glob, subprocess as sp, tkinter as tk
from tkinter import filedialog as fd
root = tk.Tk()
root.withdraw()
try:
    import psutil
except ImportError:
    print("Psutil is not installed! Installing...")
    time.sleep(0.5)
    sp.run(["pip", "install", "psutil"])
    print("Done! Doing OS install method to make sure everythings good...")
    time.sleep(0.5)
    os.system("pip install psutil")
    print("Done! Continuing...")
    time.sleep(0.5)
    os.system("cls")
import psutil
print("Checking for Roblox installation...")
time.sleep(0.5)
if not os.path.exists(os.environ['LOCALAPPDATA'] + '/Roblox'):
    print("Oops! You dont seem to have Roblox installed! Without it, this script cannot continue!")
    time.sleep(1)
    exit(1)
else:
    print("Found installation!")
    time.sleep(1)
    os.system("cls")
print("It is recommended that you backup the current 'ouch.ogg' file before continuing in case this ever breaks!")
print("Would you like to backup the file? (Y/n)")
backup = input()


if backup == "Y" or backup == "y" or backup == "":
    print("Backing up file...")
    time.sleep(0.5)
    for directory in glob.glob(os.environ['LOCALAPPDATA'] + '/Roblox/Versions/version-*/content/sounds/'):
        if os.path.exists(directory + 'ouch.ogg'):
            shutil.copy(directory + 'ouch.ogg', os.environ['USERPROFILE'] + '/Desktop/ouch.ogg.bak')
            print("Done! Saved as 'ouch.ogg.bak' on your desktop.")
    time.sleep(1)
    os.system("cls")
    print("Now, choose the file you want to use as the new 'ouch.ogg' file.")
    oggcheck = fd.askopenfilename(defaultextension=".ogg", filetypes=[("Ogg files", "*.ogg")], title="Choose a file.", initialdir="./")
    if not oggcheck.endswith(".ogg"):
        print("Oops! The file you selected is not an .ogg file! Please try again.")
        time.sleep(0.7)
        exit(1)
    else:
        print("Done! The new 'ouch.ogg' file has been selected! Renaming...")
        if os.path.exists(directory + 'ouch.ogg'):
            os.remove(directory + 'ouch.ogg')
        os.rename(os.path.basename(oggcheck), 'ouch.ogg')
        shutil.move('ouch.ogg', directory + 'ouch.ogg')
        time.sleep(1)
        os.system("cls")
        if "RobloxPlayerBeta.exe" in (p.name() for p in psutil.process_iter()):
            print("Roblox is currently running. Please close it before continuing.")
            time.sleep(0.7)
            exit(1)
elif backup == "N" or backup == "n":
    print("Backup is STRONGLY recommended, but continuing without backup...")
    time.sleep(1)
    os.system("cls")
    print("Now, choose the file you want to use as the new 'ouch.ogg' file.")
    oggcheck = fd.askopenfilename(defaultextension=".ogg", filetypes=[("Ogg files", "*.ogg")], title="Choose a file.", initialdir="./")
    for directory in glob.glob(os.environ['LOCALAPPDATA'] + '/Roblox/Versions/version-*/content/sounds/'):
        if os.path.exists(directory + 'ouch.ogg'):
            os.remove(directory + 'ouch.ogg')
    if not oggcheck.endswith(".ogg"):
        print("Oops! The file you selected is not an .ogg file! Please try again.")
        time.sleep(0.7)
        exit(1)
    else:
        print("Done! The new 'ouch.ogg' file has been selected! Renaming...")
        if os.path.exists(directory + 'ouch.ogg'):
            os.remove(directory + 'ouch.ogg')
        os.rename(os.path.basename(oggcheck), 'ouch.ogg')
        shutil.move('ouch.ogg', directory + 'ouch.ogg')
        time.sleep(1)
        os.system("cls")
        if "RobloxPlayerBeta.exe" in (p.name() for p in psutil.process_iter()):
            print("Roblox is currently running. Please close it before continuing.")
            time.sleep(0.7)
            exit(1)
        else:
            print("Everything is done! You can now open Roblox and enjoy your new modified file!")
            time.sleep(0.7)
            exit(0)
