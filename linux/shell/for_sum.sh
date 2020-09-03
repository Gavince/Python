#!/bin/bash

sum=0

for i
do
	sum=$[$sum + $i]
done
echo "Sum is : $sum"
exit 0
