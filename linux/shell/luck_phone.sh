#!/bin/bash

INFO="./phone_number.txt"

for ((i=1;i<=5;i++))
do
	line=$(wc -l $INFO | cut -d " " -f1)
	luck_line=$[$RANDOM%$line]
	luck_num=$(head -$luck_line $INFO | tail -1)
	echo $luck_num>>luck_phone_num.txt
	echo "139****${luck_num:7:4}"
done

exit 0
