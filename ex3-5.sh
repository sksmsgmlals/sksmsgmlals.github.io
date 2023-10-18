#!/bin/bash
echo '프로그램을 시작합니다.'
function_a() {
	echo "함수 안으로 들어 왔음"
	ls $1
}

function_a $1
echo '프로그램을 종료합니다.'


exit 0
