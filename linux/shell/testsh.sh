#!/bin/bash

A="Hello"
B="World"
C="Computer"

if [ "$1" == "$A" ];then
	echo "$A $B"
else
	echo "$A $C"
fi
exit 0
