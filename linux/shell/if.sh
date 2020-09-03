#!/bin/bash

read -t 30 -p "Enter a filename:" filename
echo -e "Shell name:$0\nvar nums:$#"

if [ -e $filename ];then
	echo "$filename 存在!"

elif [ $1 -lt $2 ];then
	echo -e ""$1" $1"
	echo "$filename 不存在!"

else
	echo 
fi

exit 0
