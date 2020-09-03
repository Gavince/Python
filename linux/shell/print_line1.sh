#!/bin/bash

y=1
while (($y<=5))
do
	for ((x=1;x<=6-$y;x++))
		do
			echo -n $x
		done

echo 
let y++
done


