#!/bin/bash

sum=0
while [ $# -ne 0 ]
do
	sum=$[$sum+1]
	shift
done

echo "Sum is :$sum"

exit
