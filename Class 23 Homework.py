#Practice Program
from tkinter import *
import random
window=Tk()
color=["red","orange","yellow","green","blue","#A12312","#FE0000","#317F43","#BDECB6","#7FB5B5","indigo","violet"]
window.geometry("500x500")
window.title("Random Colored Labels (Rerun code to change label colors.)")
c=random.choice(color)
lb1=Label(window,text="This is a label that has random colors.",bg=c,fg="white",font=("ariel",15,"bold"))
lb2=Label(window,text="This is a label that has random colors.",bg=c,fg="white",font=("ariel",15,"bold"))
lb1.place(x=100,y=200)
lb2.place(x=100,y=300)
window.mainloop()