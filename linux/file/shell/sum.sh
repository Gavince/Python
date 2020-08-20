#!/bin/bash

echo "Param num:$#"
echo "Name:$0"
sum=$(($1+$2))
echo "Sum is :$sum"
echo "The params:$#"
echo "The params nums is(*) :$*"
echo "The params nums is(@) :$@ "
exit 0
