#!/bin/bash

val=$(uname -r)
frist=$(echo $val | cut -d "." -f1)
second=$(echo $val | cut -d "." -f2)
echo "内核版本：$val"

if [[ $frist -gt 3 && $first -lt 6 ]];then
	if [ $second -eq 4 ];then
		echo "该内核版本为指定版本！"
	else
		echo "请升级内核版本！"
	
	fi
else
	echo "该内核版本暂不支持！"
fi 

exit 0
