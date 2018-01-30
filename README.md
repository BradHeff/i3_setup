# i3wm setup script

i3wm setup script makes setting up my i3 setup automation and easy

## Clone

If you want to run script from a local file or if you want to make your own modifications just clone the repository into your local filesystem:

    git clone https://github.com/BradHeff/i3_setup.git

## usage

to run the script you must use arguments to copy the files you want to the desired destination

to copy all the files run

    python setup.py --all


to copy just the i3lock files

    python setup.py --i3lock

to copy just the config files (neofetch, cava and ranger)

    python setup.py --config

to copy just the i3 files

    python setup.py --i3

to show the help

    python setup.py -h
