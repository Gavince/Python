#!/bin/bash

read filename

if [ -d $filename ]; then
	echo "$filename is True"
else
	echo "$filename is False"
fi

exit 0
