#Class for Bank Application
'''class Bank:
    def __init__(self):
        self.bank_database={}
        self.bank_balance={}
    def create_account(self,username,password):
        self.bank_database.update({username:password})
        self.bank_balance.update({username:5000})
        print(f"Hello {username}, you have created your bank account. Enjoy!")
    def check_balance(self,username,password):
        if password==self.bank_database[username]:
            print(f"Your available balance in your account:\n{self.bank_balance[username]}")
        else:
            print("Bank account details are not recognized.")'''

#Bank Application
class Bank:
    def __init__(self):
        self.bank_database={}
        self.bank_balance={}
    def create_account(self,username,password):
        self.bank_database.update({username:password})
        self.bank_balance.update({username:5000})
        return (f"Hello {username},\n you have created your bank account. Enjoy!")
    def check_balance(self,username,password):
        if password==self.bank_database[username]:
            return (f"Your available balance in your account:\n{self.bank_balance[username]}")
        else:
            return ("Bank account details are not recognized.")

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window1=Tk()
window1.geometry("500x500")
window1.title("Infyni Bank")
lb_txt=Label(window1,text="Hey User, welcome to Infyni Bank!",font=("Lucida",15,"bold"))

def bank_window():
    msg_alert = messagebox.askquestion("Info", "Would you like to continue to Infyni Bank?")
    if msg_alert == "yes":
        window1.withdraw()
        main_window()
    else:
        return

def main_window():
    window2 = Toplevel()
    window2.geometry("850x500")
    window2.title("Infyni Bank")
    lb_username=Label(window2,text="Username:",font=("Lucida",15,"bold"))
    lb_username.place(x=20,y=20)
    en_username=Entry(window2,font=("Lucida",15,"bold"))
    en_username.place(x=140,y=20)
    lb_password=Label(window2, text="Password:", font=("Lucida", 15, "bold"))
    lb_password.place(x=480,y=20)
    en_password=Entry(window2, font=("Lucida", 15, "bold"))
    en_password.place(x=600,y=20)
    lb_amount=Label(window2, text="Amount:", font=("Lucida", 15, "bold"))
    lb_amount.place(x=20,y=70)
    en_amount = Entry(window2, font=("Lucida", 15, "bold"))
    en_amount.place(x=140,y=70)
    lb_display=Label(window2,text="",font=("Lucida", 10, "bold"),borderwidth=2,width=50,height=10,relief = "solid")
    lb_display.place(x=110,y=120)
    ob1=Bank()

    def create_account():
        username=en_username.get()
        password=en_password.get()
        ob2=ob1.create_account(username,password)
        lb_display.config(text=ob2)

    btn_createaccount=Button(window2,text="Create Account",font=("Lucida", 10, "bold"),command=create_account)
    btn_createaccount.place(x=50,y=400)
    window2.mainloop()

btn_open=Button(window1,text="   Continue ➡️",font=("Lucida Fax",10),command=bank_window)
lb_txt.place(x=90,y=400)
btn_open.place(x=190,y=450)









window1.mainloop()