#!/bin/bash

touch DB.txt
if [ ! -d $1 ] && [ ! -d $2 ] ; then
	echo -e "$1" "$2"  >> DB.txt
fi

exit 0
