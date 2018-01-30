#!/usr/bin/env python3

# Imports
import os


# Arrays of files to check
configs = ["config/cava/config", "config/neofetch/config.conf", "config/ranger/bookmarks",
           "config/ranger/commands.py", "config/ranger/commands_full.py", "config/ranger/history",
           "config/ranger/rc.conf", "config/ranger/rifle.conf", "config/ranger/scope.sh",
           "config/ranger/tagged"]

lock = ["config/i3/lock", "config/i3/lock.png", "config/i3/lock.xcf", "config/i3/lock3.png",
        "config/i3/lock3.png"]

i3 = ["i3/config", "i3/cow.py", "i3/cowsay", "i3/getspace", "i3/i3blocks.conf", "i3/mcp.sh",
      "i3/mem", "i3/pipes.sh", "i3/showimage", "i3/theme_picker", "i3/title", "i3/vpn.sh",
      "i3/walscript", "i3/weather.sh", "i3/moveworkspace.sh"]

home = ["home/.conkyrc", "home/.Xresources", "home/.zshrc", "home/compton.conf"]


# Check file class (If a file in the array list can not be found in the directorys then
# the methods below will return False and stop the script.
class CheckFiles:

    # Check config directory
    def check_configs(self):
        print("checking .config files")
        for file in configs:
            if not os.path.isfile(file):
                return False
        return True

    # Check config/i3 directory
    def check_lock(self):
        print("checking i3lock files")
        for file in lock:
            if not os.path.isfile(file):
                return False
        return True

    # Check i3 directory
    def check_i3(self):
        print("checking i3 config files")
        for file in i3:
            if not os.path.isfile(file):
                return False
        return True

    # Check home directory
    def check_home(self):
        print("checking i3 config files")
        for file in home:
            if not os.path.isfile(file):
                return False
        return True
