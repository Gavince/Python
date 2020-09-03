#!/bin/bash

for i in {1..5}
do
	for ((j=1; j<=$i; j++))
	do
		echo -n $j
	done
	echo 
done

exit 0
