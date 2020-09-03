#!/bin/bash

read -t 30 -p "请输入一个判断的数字：" number

test $number -eq 1 && echo "$number是一个质数" && exit 
test $number -eq 2 && echo "$number是一个质数" && exit


# 循环判断是否为质数
# for ((i=1;i<100;i++))
 
for i in `seq 2 $[$number-1]`
do
	if [ $[$number%i] -eq 0 ];then
		echo ”$number不是一个是质数“
		exit
	else
		echo ”$number是一个是质数“
		exit
	fi
done

exit 0
