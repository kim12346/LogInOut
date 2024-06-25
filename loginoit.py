from tkinter import *
from tkinter import ttk



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
    global new_id_en, new_pw_en, confirm_btn, canc_btn, new_id_label, new_pw_label, grid

    grid = ttk.Separator(root, orient="horizontal")
    grid.pack(fill="both")

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
    canc_btn = Button(root, width=10, height=1, text='취소', command=cancle)
    canc_btn.pack()
def cancle():# 회원가입창 에서 취소버튼을 누르면 회원가입창 사라짐

    new_id_en.destroy() #입력 창 등 삭제
    new_pw_en.destroy()
    new_id_label.destroy()
    new_pw_label.destroy()
    confirm_btn.destroy()
    canc_btn.destroy()
    grid.destroy()


def confirm(): # 회원가입 창에서 아이디와 비번을 입력하고 확인 버튼을 눌렀을 때의 이벤트



    dict_id = new_id_en.get()
    dict_pw = new_pw_en.get()

    new_id_en.delete(0, END)
    new_pw_en.delete(0, END)

    if dict_id and dict_pw:
        list.append("{} {}".format(dict_id, dict_pw))
        with open("IDPW.txt", "a", encoding="utf8") as inf_file:
            inf_file.write("{} {}\n".format(dict_id, dict_pw))
    else:
        print("아이디 또는 패스워드를 입력하세요!")

    new_id_en.destroy() #입력 창 등 삭제
    new_pw_en.destroy()
    new_id_label.destroy()
    new_pw_label.destroy()
    confirm_btn.destroy()
    canc_btn.destroy()
    grid.destroy()

def chk_login():
    global input_id, input_pw

    input_id = id_entry.get()
    input_pw = pw_entry.get()

    try:
        with open("IDPW.txt", "r", encoding="utf8") as chkfile:
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
        infor_user()
    elif input_id not in dict:
        print("입력하신 아이디는 존재하지 않습니다.")
    elif dict[input_id] != input_pw:
        print("비밀번호가 틀립니다.")
    else:
        print("로그인 실패")


def infor_user():

    global user, profile, pro_lable, grid, pro_out, logoutbtn
    grid = ttk.Separator(root, orient="horizontal")
    grid.pack(fill="both")

    profile = PhotoImage(file="파이썬/userimg.png")
    pro_lable = Label(root, image=profile)
    pro_lable.pack()
    user = Label(root, width=20, height=1, text=f"회원 아이디: {input_id}")
    user.pack()
    logoutbtn = Button(root, text="로그아웃", command=logout)#로그아웃버튼
    logoutbtn.pack()
    pro_out = Button(root, text="회원탈퇴", command=proout) #회원탈퇴버튼
    pro_out.pack()

#test.py에 원본있음

def logout(): # 회원정보함수에서 로그아웃버튼을 눌렀을 때 로그아웃되는 함수(프로필, 입력한 정보가 사라져야됨)
    pro_lable.destroy()
    user.destroy()
    logoutbtn.destroy()
    pro_out.destroy()
    id_entry.delete(0, END)
    pw_entry.delete(0, END)
    

def proout(): # 회원탈퇴 함수(파일에 있는 아이디 지우고 로그아웃함수 포함시키기)
    pass
        

log_btn = Button(root, width=10, height=1, text="LogIn", command=chk_login)  # 로그인 버튼
log_btn.pack()

join_btn = Button(root, width=10, height=1, text="Join", command=join)  # 회원가입 버튼
join_btn.pack()

root.mainloop()