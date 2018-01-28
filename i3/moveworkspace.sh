#!/bin/sh
NONPRIMARY_SCREEN=$( xrandr -q | awk '/DisplayPort-0 connected/ {print $1}' )
PRIMARY_SCREEN=$( xrandr -q | awk '/ connected primary/ {print $1}' )

if [ -n "$NONPRIMARY_SCREEN" ] ; then
    i3-msg "move workspace to output $NONPRIMARY_SCREEN"
else
    # there is no primary screen
    i3-nagbar -m 'No primary screen defined' -t warning
fi
