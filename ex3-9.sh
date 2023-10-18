#!/bin/bash

if [ ! -d $1 ] ; then
	grep "$1" DB.txt
fi
exit 0
