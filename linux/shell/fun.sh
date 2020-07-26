#!/bin/sh

# function
print() {
	local a=$1 #定义局部变量
	echo "a=$a"
}

# main

a=5
echo "please enter a num(int)"
read -p "enter"  b
if `expr $b + 0`;then
	echo "a+b=`expr $a + $b`"
fi

print $b

exit 0
