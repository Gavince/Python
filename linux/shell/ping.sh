#!/bin/bash

read -t 30 -p "Enter a IP address:" IP

ping -c2 $IP&>./null

if [ $? -eq 0 ];then
	echo "$IP is valid!"
else
	echo "$IP is in valid!"
fi
exit 0
