#!/bin/bash

# ping10网络
NETP=10.202.144

for i in {1..10}
do
{
	ping -c3 $NETP.72 &>>./ping_info.txt
	if [ $? -eq 0 ];then
		echo "$NETP.$i is OK!" > ./up_ip.txt
	else
		echo "please check $NETP.$i">./down.ip.txt
	fi
}&
done
wait


