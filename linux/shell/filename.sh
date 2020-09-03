#!/bin/bash

declare -i -r YEAR=2020

read -t 30 -p "输入文件的路径:" filename

if [ -d $filename ]; then
	echo "$filename 目录存在！"
else
	echo "$filename 目录不存在！"
fi

echo "检查年份：${YEAR}"
echo "检查具体时间：$(date '+%F %T')"
exit 0
