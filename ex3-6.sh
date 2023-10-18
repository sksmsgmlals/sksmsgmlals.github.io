#!/bin/bash

if [ ! -d $1 ] ; then
	mkdir $1
	cd $1
	for i in {1..5}
	do
		touch file$i.txt
	done

	tar cvf $1.tar file1.txt file2.txt file3.txt file4.txt file5.txt

	mkdir $1

	mv $1.tar $1

	cd $1

	tar xvf "$1.tar"
fi


exit 0
