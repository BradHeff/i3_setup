#!/bin/bash 

if [ -d "/proc/sys/net/ipv4/conf/tun0" ]; then
	echo "On"
else
	echo "Off"
fi