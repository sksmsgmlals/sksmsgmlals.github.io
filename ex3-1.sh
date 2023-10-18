#!/bin/bash
read num
if [ $num -ge 0 ]
then
	for ((i=0; i<$num; i++))
	do
		echo 'hello world'
	done
else
	while [ 1 ]
	do
		echo 'hello world'
	done
fi 

exit 0
