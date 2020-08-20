#!/bin/bash

read filename

if [-e $filename]; then
	echo "$filename is a document!"
else
	echo "$filename is not a document!"
fi

exit 0
