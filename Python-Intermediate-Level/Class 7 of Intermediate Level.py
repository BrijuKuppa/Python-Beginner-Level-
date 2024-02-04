from tkinter import *
import random
#Rock, Paper, Scissors Game With GUI
window=Tk()
window.geometry("700x350")
window.title("Rock, Paper, Scissors")
lb_title=Label(window,text="Welcome to Rock, Paper, Scissors!",font=("courier",15,"underline"))
lb_title.place(x=160,y=10)
lb_instructions=Label(window,text="Instructions:\n Rock wins Scissors, Scissors wins Paper, and Paper wins Rock.",font=("courier",12,"italic"))
lb_instructions.place(x=40,y=40)
lb_contestants=Label(window,text=" Player",font=("courier",12,"bold"))
lb_contestants.place(x=200,y=90)
lb_vs=Label(window,text="Vs.   ",font=("courier",12,"bold"))
lb_vs.place(x=330,y=90)
lb_computer=Label(window,text=" Computer",font=("courier",12,"bold"))
lb_computer.place(x=400,y=90)
lb_whowillwin=Label(window,text="Who Will Win?",font=("courier",12,"bold"))
lb_whowillwin.place(x=280,y=120)
lb_result=Label(window,text="",font=("courier",15,"bold"),borderwidth=2,width=20,relief="solid")
lb_result.place(x=230,y=150)

computer_score=0
player_score=0
game_list=["rock","paper","scissors"]

def rock():
    global player_score
    global computer_score
    com_choice=random.choice(game_list)
    if com_choice=="rock":
        result="It's a Tie!"
    elif com_choice=="paper":
        result="Computer Wins!"
        computer_score=computer_score+1
        lb_computer_frame.config(text=computer_score)
    else:
        result="Player Wins!"
        player_score=player_score+1
        lb_player_frame.config(text=player_score)
    lb_contestants.config(text="Rock")
    lb_result.config(text=result)
    lb_computer.config(text=com_choice.title())
    btn_rock["state"]="disable"
    btn_paper["state"]="disable"
    btn_scissors["state"]="disable"

def paper():
    global player_score
    global computer_score
    com_choice=random.choice(game_list)
    if com_choice=="paper":
        result="It's a Tie!"
    elif com_choice=="rock":
        result="Computer Wins!"
        computer_score=computer_score+1
        lb_computer_frame.config(text=computer_score)
    else:
        result="Player Wins!"
        player_score = player_score+1
        lb_player_frame.config(text=player_score)
    lb_contestants.config(text="Paper")
    lb_result.config(text=result)
    lb_computer.config(text=com_choice.title())
    btn_rock["state"]="disable"
    btn_paper["state"]="disable"
    btn_scissors["state"]="disable"

def scissors():
    global player_score
    global computer_score
    com_choice=random.choice(game_list)
    if com_choice=="scissors":
        result="It's a Tie!"
    elif com_choice=="rock":
        result="Computer Wins!"
        computer_score=computer_score+1
        lb_computer_frame.config(text=computer_score)

    else:
        result="Player Wins!"
        player_score=player_score+1
        lb_player_frame.config(text=player_score)
    lb_contestants.config(text="Scissors")
    lb_result.config(text=result)
    lb_computer.config(text=com_choice.title())
    btn_rock["state"]="disable"
    btn_paper["state"]="disable"
    btn_scissors["state"]="disable"

def reset():
    btn_rock["state"]="active"
    btn_paper["state"]="active"
    btn_scissors["state"]="active"
    lb_contestants.config(text="Player")
    lb_result.config(text="")
    lb_computer.config(text="Computer")

btn_rock=Button(window,text="Rock\n🪨",font=("courier",12,"bold"),width=9,command=rock)
btn_rock.place(x=175,y=200)
btn_paper=Button(window,text="Paper\n📄",font=("courier",12,"bold"),width=9,command=paper)
btn_paper.place(x=305,y=200)
btn_scissors=Button(window,text="Scissors\n✂️",font=("courier",12,"bold"),command=scissors)
btn_scissors.place(x=430,y=200)
lb_player=Label(window,text="Player Score:",font=("courier",10,"bold"),width=10)
lb_player.place(x=180,y=270)
lb_computer_lb=Label(window,text="Computer Score:",font=("courier",10,"bold"),width=10)
lb_computer_lb.place(x=400,y=270)
lb_player_frame=Label(window,text="",font=("courier",12,"bold"),borderwidth=2,width=10,relief="solid")
lb_player_frame.place(x=180,y=300)
lb_computer_frame=Label(window,text="",font=("courier",12,"bold"),borderwidth=2,width=10,relief="solid")
lb_computer_frame.place(x=400,y=300)
btn_reset=Button(window,text="Reset",font=("courier",12,"bold"),command=reset,bg="red")
btn_reset.place(x=310,y=300)
window.mainloop()