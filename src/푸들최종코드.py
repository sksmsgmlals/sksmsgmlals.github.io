import random
import tkinter as tk
import tkinter.font
  
check_switch = 0

def switch(*args):
    global check_switch
    if check_switch == 0:
        try:
            check = int(entry_chance.get())
            start_game()
            check_switch = 1
        except:
            pass
    else:
        check_word()


def check_word():           #게임 코드
    global alpha_switch, rightword, wrongword, justplace, secret_word, county, word_label_list
    guess = entry.get()     #사용자의 답을 입력 받기

    if len(guess) != len(secret_word):
        result_label.config(text="입력한 단어의 길이가 맞지 않습니다.",bg="#FFFAF0")       #단어의 길이가 5글자가 아니면 입력받지 않음
        return
    
    max_attempts1 = entry_chance.get() # 최대 시도 횟수
    max_attempts=int(max_attempts1)-1
    feedback = ""
    for i in range(len(secret_word)):
        alpha_index = alpha_list.index(guess[i].upper())
        if guess[i] == secret_word[i]:  #만약 알파벳의 자리가 맞다면
            feedback += guess[i]        #위치를 알려주는 피드백 칸에 단어 추가
            rightword=tk.Label(root,text=f"{guess[i]}",bg="#8FBC8F",width=5,height=3)
            rightword.place(x=270+i*55,y=350+55*county)
            word_label_list.append(rightword)
            if alpha_switch[alpha_index] != 2:
                alpha_label_list[alpha_index].config(bg="#8FBC8F")
                alpha_switch[alpha_index] = 2

        elif guess[i] in secret_word:   #알파벳의 자리는 맞지 않지만 존재한다면
            feedback += "O"             #"O"로 표시
            justplace=tk.Label(root,text=f"{guess[i]}",bg="#FFA500",width=5,height=3)
            justplace.place(x=270+i*55,y=350+55*county)
            word_label_list.append(justplace)
            if alpha_switch[alpha_index] == 0:
                alpha_label_list[alpha_index].config(bg="#FFA500")
                alpha_switch[alpha_index] = 1
                
        else:                           #알파벳이 단어에 존재하지 않는다면
            feedback += "X"             #"X"로 표시
            wrongword=tk.Label(root,text=f"{guess[i]}",bg="#DDE7E7",width=5,height=3)
            wrongword.place(x=270+i*55,y=350+55*county)
            word_label_list.append(wrongword)
            alpha_label_list[alpha_index].config(bg="grey")
            alpha_switch[alpha_index] = -1

    resultfont=tk.font.Font(size=15)
    if guess == secret_word:            #답과 단어가 일치한다면
        result_label.config(text="정답입니다.",width=20, bg="#FFFAF0")  #정답이라고 표기
    elif len(guesses) >= max_attempts:      #시도 횟수를 초과하면 답을 공개
        result_label.config(text=f"시도 횟수 초과! 정답은 {secret_word}입니다.", bg="#FFFAF0")
    else:
        guesses.append(guess)
    county+=1
    entry.delete(0,tk.END)

county=0
word_label_list = []
guesses = []


def new_game():         #새로운 게임 시작하기
    global secret_word, guesses, county, word_label_list
    guesses = []
    result_label.config(text="", bg="#FDF2B3")
    entry.delete(0, 'end')
    county=0
    for i in alpha_label_list:
        i.config(bg="#FFFAF0")
    for i in word_label_list:
        i.destroy()
    word_label_list = []
    secret_word = random.choice(word_list)
    

def start_game():       #시작하기 전 닉네임 입력받기
    global player_name, secret_word
    player_name = entry_name.get()

    if player_name:
        name_label.config(text=f"플레이어: {player_name}",bg="#FFFAF0")
        entry_chance.pack_forget()
        chance_label.pack_forget()
        entry_name.pack_forget()
        start_button.pack_forget()
        word_label.pack()
        entry.pack()
        check_button.pack()
        feedback_label.pack()
        result_label.pack()
        new_game_button.pack()
        entry.focus()
        for i in range(len(alpha_label_list)-4):
            alpha_label_list[i].place(x=100+i%11*55, y=750+i//11*55, width=50,height=50)
        alpha_label_list[22].place(x=305,y=860,width=50,height=50)
        alpha_label_list[23].place(x=360,y=860,width=50,height=50)
        alpha_label_list[24].place(x=415,y=860,width=50,height=50)
        alpha_label_list[25].place(x=470,y=860,width=50,height=50)
        secret_word = random.choice(word_list)
    result_label.config(text="", bg="#FDF2B3")

root = tk.Tk()
root.title("Foodle Game")
root.geometry("800x950")  # 창의 크기 설정
root.resizable(False, False)

root.configure(bg="#FDF2B3")

player_name = ""
read_file = open('isalpha.txt','r',encoding='UTF8')
word_file = read_file.read()
word_list = list(word_file.split('\n'))             # 단어 목록

spacer = tk.Label(width=10,height=5,bg="#FDF2B3") # 여백을 주기 위한 빈 라벨 생성
spacer.pack()

font=tk.font.Font(family="stencil",size=30)
foodle_label=tk.Label(root, text="FOODLE",width=17,height=1,font=font,bg="#FFD700",fg="#C71585",relief="ridge")
foodle_label.pack()

frame = tk.Frame(root, padx=10, pady=5,bg="#FDF2B3")
frame.pack()

spacer = tk.Label(frame, width=10,bg="#FDF2B3") # 여백을 주기 위한 빈 라벨 생성
spacer.pack()

name_label = tk.Label(root, text="플레이어 이름",width=20, bg="#FFFAF0")
name_label.pack()

entry_name = tk.Entry(root)     #이름 입력 받기
entry_name.pack()
entry_name.focus()

chance_label = tk.Label(root, text="시도 횟수(8번 이하)",width=20, bg="#FFFAF0")
chance_label.pack()

entry_chance= tk.Entry(root)    #시도 횟수 입력받기
entry_chance.pack()

alpha_list =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_switch = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alpha_label_list = []
for i in alpha_list:
    alpha_label_list.append(tk.Label(root, text=i, width=20, bg='#FFFAF0'))


spacer = tk.Label(width=10,bg="#FDF2B3") # 여백을 주기 위한 빈 라벨 생성
spacer.pack()

start_button = tk.Button(root, text="게임 시작", command=start_game,width=10, bg="#FFFAF0")
start_button.pack()

word_label = tk.Label(root, text="답 입력하기:", bg="#FFFAF0")
entry = tk.Entry(root)
check_button = tk.Button(root, text="확인", command=check_word, bg="#FFFAF0")
feedback_label = tk.Label(root, text="", bg="#FDF2B3")
result_label = tk.Label(root, text="", bg="#FFFAF0")
new_game_button = tk.Button(root, text="다시하기", command=new_game, bg="#FFFAF0")
guesses_label = tk.Label(root, text="", bg="#FFFAF0")
trys_label=tk.Label(root,text="", bg="#FFFAF0")

root.bind('<Return>', switch)
root.mainloop()