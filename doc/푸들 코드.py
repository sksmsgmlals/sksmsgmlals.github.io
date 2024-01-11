
import random

read_file = open('isalpha.txt','r',encoding='UTF8')
word_file = read_file.read()
word_list = list(word_file.split('\n'))

x=random.choice(word_list)

chance=int(input("몇 번만에 맞출 수 있나요?"))
if x in word_list:
    cn=0
    while cn==chance:
        answer = input("단어를 입력하시오")    
        for i in range(5):
            if x[i] == answer[i]:
                print(f"{i+1}자리 정답입니다.")
            elif x[i] in answer:
                print("자리는 맞지 않지만 존재합니다.")
            else:
                print("존재하지 않습니다.")
        cn+=1
        if answer==x:
            print("정답입니다.")
            break
else:
    print("프랑스어가 아닙니다.")

