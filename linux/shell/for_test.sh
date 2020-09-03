#!/bin/bash

sum=0
# for ((i=1;i<10;i++))
for i in {1..10..2}
do	
	sum=$[$i+$sum]
	if [ $sum -eq 16 ];then
		echo "touch a file"
		if [ -e $sum.py ];then
			rm -rf $sum.py
		else
			touch $sum.py
		sleep 2
		echo "文件已经创建"
		fi
	else
		echo "continue"
	fi
	echo "$i, $sum"

done
