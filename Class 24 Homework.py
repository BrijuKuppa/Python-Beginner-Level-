#Practice Program: Sign In
#NOTE: MAKE SURE YOU PUT THE USERNAME AS "Infyni" AND EMAIL ADRESS AS "infyni.coding@gmail.com" AND PASSWORD AS "infyni123"
from tkinter import *
from tkinter import messagebox

def verify():
    username=ent1.get()
    email=ent2.get()
    password=ent3.get()
    if username=="Infyni" and email=="infyni.coding@gmail.com" and password=="infyni123":
        mesg = f"Welcome {username}, you have signed in."
        messagebox.showinfo("Sign In",mesg)
    else:
        mesg=f"The info you put in the forms is wrong. Please try again."
        messagebox.showwarning("Sign In", mesg)

window=Tk()
window.geometry("400x500")
window.config(bg="black")
window.title("Sign In")
lb1=Label(window,text="Sign In:",font=("Courier New Baltic",17,"bold"),bg="black",fg="white")
lb2=Label(window,text="Username:",font=("Courier New Baltic",15),bg="black",fg="white")
lb3=Label(window,text="Email Address:",font=("Courier New Baltic",15),bg="black",fg="white")
lb4=Label(window,text="Password:",font=("Courier New Baltic",15),bg="black",fg="white")
ent1=Entry(window,font=("Courier New Baltic",15,"bold"),bg="white",fg="black")
ent2=Entry(window,font=("Courier New Baltic",15,"bold"),bg="white",fg="black")
ent3=Entry(window,font=("Courier New Baltic",15,"bold"),bg="white",fg="black",show="*")
bt=Button(window,text="Sign In",font=("Courier New Baltic",15,"bold"),bg="black",fg="white",command=verify)
lb1.pack()
lb2.pack(pady=5)
ent1.pack(pady=3)
lb3.pack(pady=3)
ent2.pack(pady=3)
lb4.pack(pady=3)
ent3.pack(pady=3)
bt.pack(pady=10)
window.mainloop()