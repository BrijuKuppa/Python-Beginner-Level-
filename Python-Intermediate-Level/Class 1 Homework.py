#2-Number Calculator
from ttkbootstrap import *
from ttkbootstrap.constants import *
def add():
    ent3.delete(0,END)
    a=float(ent1.get())
    b=float(ent2.get())
    c=a+b
    ent3.insert(END,c)

def sub():
    ent3.delete(0,END)
    a=float(ent1.get())
    b=float(ent2.get())
    c=a-b
    ent3.insert(END,c)

def mul():
    ent3.delete(0,END)
    a=float(ent1.get())
    b=float(ent2.get())
    c=a*b
    ent3.insert(END,c)

def div():
    ent3.delete(0,END)
    a=float(ent1.get())
    b=float(ent2.get())
    c=a/b
    ent3.insert(END,c)

def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)

window=Window()
window.geometry("700x500")
window.config(bg="white")
window.title("Two-Number Calculator")
title=Label(window,text="Two-Number Calculator",bootstyle=DARK,font=("",15,"underline"))
instructions=Label(window,text="Enter two numbers and either add, subtract, multiply, or divide them.",bootstyle=DARK,font=("",12,"italic"))
lb1=Label(window,text="First Number:",bootstyle=DARK,font=("",12))
lb2=Label(window,text="Second Number:",bootstyle=DARK,font=("",12))
ent1=Entry(window,bootstyle=DARK,font=("",12))
ent2=Entry(window,bootstyle=DARK,font=("",12))
btn1=Button(window,text="Add\n ➕",bootstyle=DARK,command=add)
btn2=Button(window,text="Subtract\n    ➖",bootstyle=DARK,command=sub)
lb3=Label(window,text="Result:",bootstyle=DARK,font=("",12))
ent3=Entry(window,bootstyle=DARK,font=("",12),width=30)
btn3=Button(window,text="Multiply\n    ✖️",bootstyle=DARK,command=mul)
btn4=Button(window,text="Divide\n   ➗",bootstyle=DARK,command=div)
btn5=Button(window,text="Clear",bootstyle=DARK,command=clear)
title.pack()
instructions.pack()
lb3.pack(pady=210)
lb1.place(x=50,y=90)
ent1.place(x=180,y=90)
lb2.place(x=50,y=200)
ent2.place(x=205,y=200)
btn1.place(x=50,y=135)
btn2.place(x=120,y=135)
btn3.place(x=215,y=135)
btn4.place(x=310,y=135)
ent3.place(x=170,y=300)
btn5.place(x=310,y=350)
window.mainloop()