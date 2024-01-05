#Sign Up
from tkinter import messagebox
def verify():
    username=en1.get()
    email=en2.get()
    password=en3.get()
    if username=="" or email=="" or password=="":
        mesg = f"Please fill out all the forms."
        messagebox.showwarning("Create an Account", mesg)
    else:
        mesg=f"Hey {username}, you have created an account."
        messagebox.showinfo("Create an Account",mesg)

index=0

def show():
    global index
    s=["","*"]
    en3.config(show=s[index])
    index=index+1
    if index==2:
        index=0


from tkinter import *
window=Tk()
window.geometry("400x500")
window.config(bg="black")
window.title("Sign Up")
lb1=Label(window,text="Create an Account",font=("Courier New Baltic",15,"bold"),bg="black",fg="white")
lb1.pack()
lb2=Label(window,text="Username:",font=("Courier New Baltic",15),bg="black",fg="white")
lb2.pack()
en1=Entry(window,font=("Courier New Baltic",15))
en1.pack(pady=5)
lb3=Label(window,text="Email Address:",font=("Courier New Baltic",15),bg="black",fg="white")
lb3.pack()
en2=Entry(window,font=("Courier New Baltic",15))
en2.pack(pady=5)
lb4=Label(window,text="Password:",font=("Courier New Baltic",15),bg="black",fg="white")
lb4.pack()
en3=Entry(window,font=("Courier New Baltic",15),show="*")
en3.pack(pady=5)
bt=Button(window,text="Create Account",font=("Courier New Baltic",15,"bold"),bg="black",fg="white",command=verify)
bt.pack(pady=5)
btshow=Button(window,text="👀",font=("Courier New Baltic",12,"bold"),bg="black",fg="white",command=show)
btshow.place(x=310,y=195)
window.mainloop()