#Graphical User Interface (GUI)
from tkinter import *
import random
color=["red","orange","yellow","green","blue","#A12312","#FE0000","#317F43","#BDECB6","#7FB5B5","indigo","violet"]
window=Tk()
window.title("Graphical User Interface (GUI)")
window.geometry("1000x1000")
window.config(bg="#4CB9E7")
lb1=Label(window,text="Press the button to randomize the color of this label.",bg="orange",fg="white",font=("Great Vibes",15,"bold"))
lb1.place(x=350,y=200)
def change_color():
    c=random.choice(color)
    lb1.config(bg=c)
button=Button(window,text="Button",bg="orange",fg="white",font=("Great Vibes",15,"bold"),command=change_color)
button.place(x=490,y=400)
window.mainloop()