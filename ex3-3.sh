#!/bin/bash
bmi=`expr $1 \* 100000 / $2 / $2`
if [[ $bmi -ge 180 ]] && [[ $bmi -lt 230 ]]
then
	echo "정상체중입니다"
elif [[ $bmi -lt  180 ]]
then
	echo "저체중입니다"
elif [[ $bmi -ge 230 ]]
then
	echo "과체중입니다."

fi

exit 0
