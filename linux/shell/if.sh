#!/bin/bash

read filename

if [-d $filename]; then
	echo "$filename is a document!"
else
	echo "$filename is not a document!"
fi

exit 0
