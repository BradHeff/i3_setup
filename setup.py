#!/usr/bin/env python3

# Imports
import os
import sys
import shutil

# global declares
HOME = "/home/pheonix/"     # Path must end with /
SCRIPT_DIR = os.path.realpath(__file__)        # get the script path **(do not change)**
DEBUG = False       # enable / disable shutil functions


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
    print("--config         install only the .configuration files")
    print("")
    print("Use -h to see commands again")


# copy the i3 configuration files
def copy_i3_config():
    if not os.path.exists(HOME + ".i3"):
        os.makedirs(HOME + ".i3")

    for fl in os.listdir("i3/"):
        if not DEBUG:
            shutil.copy("i3/" + fl, HOME + ".i3/" + fl)
        print("Copying i3/" + fl + " to " + HOME + ".i3/" + fl)

    for fl in os.listdir(os.path.dirname(SCRIPT_DIR)):
        if not os.path.isdir(fl):
            if not fl == "setup.py":
                if not DEBUG:
                    shutil.copy(fl, HOME + fl)
                print("Copying " + fl + " to " + HOME + fl)


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
    if not os.path.exists(HOME + ".config"):
        os.makedirs(HOME + ".config")
    for fl in os.listdir("config"):
        if os.path.isdir("config/" + fl):
            if not DEBUG:
                shutil.copytree("config/" + fl, HOME + ".config/" + fl)
            if not fl == "i3":
                print("Copying config/" + fl + " to " + HOME + ".config/" + fl)


# run the script
if __name__ == '__main__':
    Setup(sys.argv)
