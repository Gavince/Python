#!/bin/bash

for i in {1..1000}
do
	n1=$[$RANDOM%10]	
	n2=$[$RANDOM%10]
	n3=$[$RANDOM%10]
	n4=$[$RANDOM%10]
	n5=$[$RANDOM%10]
	n6=$[$RANDOM%10]
	n7=$[$RANDOM%10]
	echo "139$n1$n2$n3$n4$n5$n6$n7" | tee -a phone_number.txt
done


