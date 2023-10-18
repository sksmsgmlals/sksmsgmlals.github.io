#!/bin/bash
if [ "$2" == "+" ]
then
	sum=`expr $1 + $3`
	echo "$sum"
elif [ "$2" == "-" ]
then
	sum=`expr $1 - $3`
	echo "$sum"
fi

exit 0
