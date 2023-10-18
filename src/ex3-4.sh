#!/bin/bash
echo '리눅스가 재미있나요 (yes/no)'
read a
case $a in
	[no]*)
		echo "no"
		;;
	[yes]*)
		echo "yes"
		;;
	[Y]*)
		echo "yes"
		;;
	[N]*)
		echo "no"
		;;
	* )
		echo "yes or no로 입력해주세요"
		;;
esac

exit 0

