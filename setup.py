#!/usr/bin/env python3

# Imports
import os
import sys
import shutil
import classes

# global declares
HOME = "/home/pheonix/"     # Path must end with / (change to your home directory
SCRIPT_DIR = os.path.realpath(__file__)        # get the script path **(do not change)**
DEBUG = False       # enable / disable debuging (if enabled the script will NOT copy the files)


def Setup(argv):
    print("================================================")
    print("=              i3wm Setup script               =")
    print("================================================")

    if not len(sys.argv) > 1:
        showhelp(False)
    else:
        for arg in argv:
            if not arg == os.path.basename(SCRIPT_DIR) and not arg == "./setup.py":
                if arg == "--all":
                    copy_i3_config()
                    copy_i3lock()
                    copy_configs()
                    print("======================")
                    print("DONE!")
                elif arg == "--i3":
                    copy_i3_config()
                    print("======================")
                    print("DONE!")
                elif arg == "--config":
                    copy_configs()
                    print("======================")
                    print("DONE!")
                elif arg == "--i3lock":
                    copy_i3lock()
                    print("======================")
                    print("DONE!")
                elif arg == "-h":
                    showhelp(True)
                else:
                    showhelp(False)


# help commands
def showhelp(bools):
    if not bools:
        print("usage: setup.py [--options]")
    else:
        print("example: \n"
              "1)./setup.py --all\n"
              "2) python setup.py --all")
    print("---------------------------------")
    print("--all            install all configuration files")
    print("--i3             install only the .i3 config and ~/ configuration files")
    print("--i3lock         install only the i3lock files ~/.config/i3")
    print("--config         install only the .config files ~/.config/*")
    print("")
    print("Use -h to see commands again")


# copy the i3 configuration files
def copy_i3_config():
    if not os.path.exists(HOME + ".i3"):
        os.makedirs(HOME + ".i3")

    for fl in os.listdir("i3/"):
        if os.path.isfile("i3/" + fl):
            if not DEBUG:
                shutil.copy("i3/" + fl, HOME + ".i3/" + fl)
            print("Copying i3/" + fl + " to " + HOME + ".i3/" + fl)

    for fl in os.listdir("home/"):
        if os.path.isfile("home/" + fl):
            if not DEBUG:
                shutil.copy("home/" + fl, HOME + fl)
            print("Copying home/" + fl + " to " + HOME + fl)


# copy the i3lock files
def copy_i3lock():
    if not os.path.exists(HOME + ".config/i3"):
        os.makedirs(HOME + ".config/i3")

    for fl in os.listdir("config/i3"):
        if not DEBUG:
            shutil.copy("config/i3/" + fl, HOME + ".config/i3/" + fl)
        print("Copying config/i3/" + fl + " to " + HOME + ".config/i3/" + fl)


# copy the /home configuration files
def copy_configs():
    if not os.path.exists(HOME + ".config/neofetch"):
        os.makedirs(HOME + ".config/neofetch")
    if not os.path.exists(HOME + ".config/cava"):
        os.makedirs(HOME + ".config/cava")
    if not os.path.exists(HOME + ".config/ranger"):
        os.makedirs(HOME + ".config/ranger")

    for fl in os.listdir("config/neofetch"):
        if os.path.isfile("config/neofetch/" + fl):
            if not DEBUG:
                shutil.copy("config/neofetch/" + fl, HOME + ".config/neofetch" + fl)
            print("Copying config/neofetch/" + fl + " to " + HOME + ".config/neofetch/" + fl)

    for fl in os.listdir("config/ranger"):
        if os.path.isfile("config/ranger/" + fl):
            if not DEBUG:
                shutil.copy("config/ranger/" + fl, HOME + ".config/ranger" + fl)
            print("Copying config/ranger/" + fl + " to " + HOME + ".config/ranger/" + fl)

    for fl in os.listdir("config/cava"):
        if os.path.isfile("config/cava/" + fl):
            if not DEBUG:
                shutil.copy("config/cava/" + fl, HOME + ".config/cava" + fl)
            print("Copying config/cava/" + fl + " to " + HOME + ".config/cava/" + fl)


# run the script
if __name__ == '__main__':
    nothelp = True
    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg == "-h":
                nothelp = False

        if nothelp:
            files = classes.CheckFiles()
            if files.check_configs() and files.check_i3() and files.check_lock() \
                    and files.check_home():
                print("---------------------------------")
                print("Check Success ........")
                print("---------------------------------")
            else:
                print("some config files not found")
    Setup(sys.argv)

