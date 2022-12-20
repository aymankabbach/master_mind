from faulthandler import disable
import random
from random import shuffle
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Master Mind")
winner=False
buttons_list=[]
colors=["Yellow","Purple","Pink","Red","Blue","Green"]
machine_color=[]
machine_color1=[]
def machine_chooses_colors():
    for x in range(4):
        chosing_color=random.choice(colors)
        machine_color.append(chosing_color)
machine_chooses_colors()
machine_color1=[color for color in machine_color]
color=" "
def choose_color(button):
    global color
    color=button["text"]
button_a=Button(window, text=colors[0], height=4, width=8, bg='#BEB8B7', fg="black", command=lambda: choose_color(button_a))
button_a.grid(row=0 , column =0)

button_b=Button(window, text=colors[1], height=4, width=8, bg='#BEB8B7', fg="black",command=lambda: choose_color(button_b))
button_b.grid(row=0 , column =1)

button_c=Button(window, text=colors[2], height=4, width=8, bg='#BEB8B7', fg="black",command=lambda: choose_color(button_c))
button_c.grid(row=0 , column =2)

button_d=Button(window, text=colors[3], height=4, width=8, bg='#BEB8B7', fg="black",command=lambda: choose_color(button_d))
button_d.grid(row=0 , column =4)

button_e=Button(window, text=colors[4], height=4, width=8, bg='#BEB8B7', fg="black",command=lambda: choose_color(button_e))
button_e.grid(row=0 , column =5)

button_f=Button(window, text=colors[5], height=4, width=8, bg='#BEB8B7', fg="black",command=lambda: choose_color(button_f))
button_f.grid(row=0 , column =6)

def play_color(Button):
    global color
    Button["text"]=color
POS=1
button_A=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_A))
button_A.grid(row=POS,column =0)

button_B=Button(window, text="", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_B))
button_B.grid(row=POS,column =1)

button_C=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_C))
button_C.grid(row=POS,column =2)

button_D=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_D))
button_D.grid(row=POS,column =3)

button_E=Button(window, text="PLAY", height=3, width=6, bg='#BEB8B7', fg="black", command=lambda: confirm_colors())
button_E.grid(row=POS,column=6)

button_F=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black")
button_F.grid(row=POS,column =5)

buttons_list.append(button_A)
buttons_list.append(button_B)
buttons_list.append(button_C)
buttons_list.append(button_D)
buttons_list.append(button_E)
buttons_list.append(button_F)

player_color=[]
player_color1=[]
def confirm_colors():
    if button_A["text"] and button_B["text"] and button_C["text"] and button_D["text"] in colors:
        global player_color, player_color1
        player_color=[button_A["text"],button_B["text"],button_C["text"],button_D["text"]]
        button_A.config(state=DISABLED)
        button_B.config(state=DISABLED)
        button_C.config(state=DISABLED)
        button_D.config(state=DISABLED)
        player_color1=player_color
        judging()
        check_win()
judgment=[]
def judging():
    pos=0
    POS=0
    while POS<4:
        if player_color1[pos] == machine_color1[pos]:
            judgment.append("B")
            player_color1.remove(player_color1[pos])
            machine_color1.remove(machine_color1[pos])
        else:
            pos+=1
        POS+=1
    pos=0
    while len(judgment)<4:
        if player_color1[pos] in machine_color1:
            judgment.append("W")
            machine_color1.remove(player_color1[pos])
            pos+=1
        else:
            judgment.append("N")
            pos+=1
    random.shuffle(judgment)
    button_F["text"]=judgment
    button_E.config(state=DISABLED)
TRY=0
def retry():
    global POS,TRY,judgment,player_color,machine_color1,machine_color,button_A,button_B,button_C,button_D,button_E,button_F,buttons_list
    TRY+=1
    if winner == False:
        POS+=1
        button_A=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_A))
        button_A.grid(row=POS,column =0)

        button_B=Button(window, text="", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_B))
        button_B.grid(row=POS,column =1)

        button_C=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_C))
        button_C.grid(row=POS,column =2)

        button_D=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_D))
        button_D.grid(row=POS,column =3)

        button_E=Button(window, text="PLAY", height=3, width=6, bg='#BEB8B7', fg="black", command=lambda: confirm_colors())
        button_E.grid(row=POS,column=6)

        button_F=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black")
        button_F.grid(row=POS,column =5)
        buttons_list.append(button_A)
        buttons_list.append(button_B)
        buttons_list.append(button_C)
        buttons_list.append(button_D)
        buttons_list.append(button_E)
        buttons_list.append(button_F)
        judgment.clear()
        player_color.clear()
        machine_color1=[color for color in machine_color]
def check_win():
    global TRY,winner
    if judgment==["B","B","B","B"]:
        winner=True
        messagebox.showinfo("info","you win")
    else:
        if TRY==9:
            showing_result=f"the colors :{machine_color}"
            messagebox.showinfo("info",f'Game over\n{showing_result}')
        else:
            retry()
def reset():
    global button_A,button_B,button_C,button_D,button_E,button_F,POS,color,TRY,judgment,player_color,machine_color,machine_color1,buttons_list
    pos=0
    while pos<len(buttons_list):
        buttons_list[pos].destroy()
        pos+=1
    buttons_list.clear()
    color=" "
    judgment.clear()
    player_color.clear()
    machine_color.clear()
    machine_chooses_colors()
    machine_color1=[color for color in machine_color]
    TRY=0
    POS=1
    button_A=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_A))
    button_A.grid(row=POS,column =0)

    button_B=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_B))
    button_B.grid(row=POS,column =1)

    button_C=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_C))
    button_C.grid(row=POS,column =2)

    button_D=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black",command=lambda: play_color(button_D))
    button_D.grid(row=POS,column =3)

    button_E=Button(window, text="PLAY", height=3, width=6, bg='#BEB8B7', fg="black", command=lambda: confirm_colors())
    button_E.grid(row=POS,column=6)

    button_F=Button(window, text=" ", height=3, width=6, bg='#BEB8B7', fg="black")
    button_F.grid(row=POS,column =5)
main_menu=Menu(window)
window.config(menu=main_menu)
options=Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Options", menu=options)
options.add_command(label="play again", command=lambda: reset())
window.mainloop()