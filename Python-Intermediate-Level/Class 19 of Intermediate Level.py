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
            return (f"Your available balance in your account:\n${self.bank_balance[username]}")
        else:
            return ("Error: Bank account details are not recognized.")
    def deposit(self,username,password,amount):
        if password==self.bank_database[username]:
            self.bank_balance[username]=self.bank_balance[username]+amount
            return (f"Your original amount in your bank was ${self.bank_balance[username]-amount}. \nNow, after your deposit (${amount}), your acount has a balance of ${self.bank_balance[username]}")
        else:
            return ("Error: Bank account details are not recognized.")

    def withdraw(self,username,password,amount):
        if password==self.bank_database[username]:
            if self.bank_balance[username]-amount>0:
                self.bank_balance[username]=self.bank_balance[username]-amount
                return (f"Your original amount in your bank was ${self.bank_balance[username]+amount}. \nNow, after your withdraw (${amount}), your acount has a balance of ${self.bank_balance[username]}")
            else:
                return ("Error: Insufficient balance.")
        else:
            return ("Error: Bank account details are not recognized.")


from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window1=Tk()
window1.geometry("500x500")
window1.title("Infyni Bank")
lb_txt=Label(window1,text="Hey User, welcome to Infyni Bank!",font=("Lucida",15,"bold"))
image=Image.open("logo.jpg")
image=ImageTk.PhotoImage(image)
logo=Label(window1,image=image)
logo.place(x=165,y=100)

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
    lb_amount=Label(window2, text="Amount \n(In Dollars):", font=("Lucida", 15, "bold"))
    lb_amount.place(x=20,y=60)
    en_amount = Entry(window2, font=("Lucida", 15, "bold"))
    en_amount.place(x=140,y=70)
    lb_display=Label(window2,text="",font=("Lucida", 10, "bold"),borderwidth=2,width=80,height=10,relief = "solid")
    lb_display.place(x=110,y=130)
    ob1=Bank()

    def create_account():
        username=en_username.get()
        password=en_password.get()
        if username=="" or password=="":
            lb_display.config(text="Error: Enter all the required fields.")
        else:
            ob2=ob1.create_account(username,password)
            lb_display.config(text=ob2)

    def check_balance():
        username = en_username.get()
        password = en_password.get()
        if username == "" or password == "":
            lb_display.config(text="Error: Enter all the required fields.")
        else:
            ob2 = ob1.check_balance(username, password)
            lb_display.config(text=ob2)

    def deposit():
        username = en_username.get()
        password = en_password.get()
        amount = int(en_amount.get())
        if username == "" or password == "":
            lb_display.config(text="Error: Account information not recognized.")
        else:
            ob2 = ob1.deposit(username, password, amount)
            lb_display.config(text=ob2)

    def withdraw():
        username = en_username.get()
        password = en_password.get()
        amount = int(en_amount.get())
        if username == "" or password == "":
            lb_display.config(text="Error: Account information not recognized.")
        else:
            ob2 = ob1.withdraw(username, password, amount)
            lb_display.config(text=ob2)

    btn_create_account=Button(window2,text="Create Account",font=("Lucida", 10, "bold"),command=create_account)
    btn_create_account.place(x=50,y=400)
    btn_check_balance=Button(window2,text="Check Balance",font=("Lucida", 10, "bold"),command=check_balance)
    btn_check_balance.place(x=180,y=400)
    btn_deposit = Button(window2, text="Deposit Amount", font=("Lucida", 10, "bold"), command=deposit)
    btn_deposit.place(x=310, y=400)
    btn_deposit = Button(window2, text="Withdraw Amount", font=("Lucida", 10, "bold"), command=withdraw)
    btn_deposit.place(x=440, y=400)
    window2.mainloop()

btn_open=Button(window1,text="   Continue ➡️",font=("Lucida Fax",10),command=bank_window)
lb_txt.place(x=90,y=400)
btn_open.place(x=190,y=450)









window1.mainloop()