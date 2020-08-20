#!/bin/bash


read -p "Please enter choice:" val

echo -e "a:\c"
read a
echo -e "b:\c"
read b
echo -e "c:\c"
read c
echo -e "d:\c"
read d
echo -e "e:\c"
read e

echo "$val"
case $val in
	'1')echo "you enter num 1";;
	'2')echo "you enter num 2";;
	*)echo "Error!"
esac
exit 0
