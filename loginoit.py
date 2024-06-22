from tkinter import *

dict = {}
list = []


root = Tk()
root.geometry("500x500+500+140")  # 창 크기: 500x500, 창 위치: 500+140
root.title("LOGIN")  # 창 제목: LOGIN

id_label = Label(root, text="ID: ")
id_label.pack()

id_entry = Entry(root, width=30)
id_entry.pack()

pw_label = Label(root, text="PW: ")
pw_label.pack()

pw_entry = Entry(root, width=30, show="*")
pw_entry.pack()

def join():
    print("회원가입창입니다.")
    global new_id_en, new_pw_en, confirm_btn

    new_id_label = Label(root, text="New ID: ")
    new_id_label.pack()
    
    new_id_en = Entry(root, width=30)
    new_id_en.pack()
    
    new_pw_label = Label(root, text="New PW: ")
    new_pw_label.pack()
    
    new_pw_en = Entry(root, width=30, show="*")
    new_pw_en.pack()

    confirm_btn = Button(root, width=10, height=1, text="확인", command=confirm)
    confirm_btn.pack()

def confirm(): # 회원가입 창에서 아이디와 비번을 입력하고 확인 버튼을 눌렀을  때의 이벤트
    dict_id = new_id_en.get()
    dict_pw = new_pw_en.get()

    new_id_en.delete(0, END)
    new_pw_en.delete(0, END)

    if dict_id and dict_pw:
        list.append("{} {}".format(dict_id, dict_pw))
        with open("inf.txt", "a", encoding="utf8") as inf_file:
            inf_file.write("{} {}\n".format(dict_id, dict_pw))
    else:
        print("아이디 또는 패스워드를 입력하세요!")

def chk_login():
    global input_id, input_pw

    input_id = id_entry.get()
    input_pw = pw_entry.get()

    try:
        with open("inf.txt", "r", encoding="utf8") as chkfile:
            for line in chkfile:
                tmp = line.rstrip().split()

                d_id = tmp[0]
                d_pw = tmp[1]

                dict[d_id] = d_pw

    except FileNotFoundError:
        print("회원가입 기록이 없습니다.")
        return

    if input_id in dict and dict[input_id] == input_pw:
        print("로그인 성공!")
    elif input_id not in dict:
        print("입력하신 아이디는 존재하지 않습니다.")
    elif dict[input_id] != input_pw:
        print("비밀번호가 틀립니다.")
    else:
        print("로그인 실패")

log_btn = Button(root, width=10, height=1, text="LogIn", command=chk_login)  # 로그인 버튼
log_btn.pack()

join_btn = Button(root, width=10, height=1, text="Join", command=join)  # 회원가입 버튼
join_btn.pack()

root.mainloop()