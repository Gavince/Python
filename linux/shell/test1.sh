#!/bin/bash

rate=$(df -h | grep /dev/sda10 | awk '{print $5}' | cut -d "%" -f1)
if [ $rate -ge 50 ]; then
	echo "容量不够"
else
	echo "容量足够"
fi

exit 0
