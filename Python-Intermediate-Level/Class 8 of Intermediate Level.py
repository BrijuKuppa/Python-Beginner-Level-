#US Dollers Cash Tally
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window1=Tk()
window1.geometry("650x500")
window1.title("Denomination Computer")
image=Image.open("Denomination-Count.jpg")
image=ImageTk.PhotoImage(image)
lb=Label(window1,image=image)
lb.place(x=100,y=50)
lb_txt=Label(window1,text="Hey User, welcome to Denomination Computer!",font=("courier",15,"bold"))
lb_txt.place(x=70,y=400)

def message_new_window():
    msg_alert=messagebox.askquestion("Alert","Do you want to enter into Denomination Computer?")
    if msg_alert=="yes":
        window1.withdraw()
        window_to_2()
    else:
        return

def window_to_2():
    window2=Toplevel()
    window2.geometry("650x500")
    window2.title("Denomination Computer")
    lb_title=Label(window2,text="Denomination Computer",font=("courier",15,"underline","bold"))
    lb_title.place(x=180,y=10)
    lb_amount=Label(window2,text="Enter total amount of U.S Dollars here:",font=("courier",13,""))
    lb_amount.place(x=30,y=50)
    en_amount=Entry(window2,font=("courier",13,""),width=15)
    en_amount.place(x=430,y=50)
    def calculate():
        amount=int(en_amount.get())
        n_1000=amount//1000
        amount=amount%1000
        n_100=amount//100
        amount=amount%100
        n_10=amount//10
        amount=amount%10
        n_1=amount//1
        amount=amount%1
        lb_result_1000.config(text=n_1000)
        lb_result_100.config(text=n_100)
        lb_result_10.config(text=n_10)
        lb_result_1.config(text=n_1)
    btn_calculate=Button(window2,text="Calculate",font=("courier",10),bg="green",fg="white",command=calculate)
    btn_calculate.place(x=250,y=100)
    lb_result=Label(window2,text="Result:",font=("courier",15,"underline"))
    lb_result.place(x=250,y=150)
    lb_1000=Label(window2,text="$1000:",font=("courier",15))
    lb_1000.place(x=100,y=200)
    lb_result_1000=Label(window2,text="",font=("courier",15),borderwidth=2,width=10,relief="solid")
    lb_result_1000.place(x=400,y=200)
    lb_line1=Label(window2,text="_______________________________________________",font=("courier",15,"underline"))
    lb_line1.place(x=40,y=230)
    lb_100=Label(window2, text="$100:", font=("courier", 15))
    lb_100.place(x=100,y=280)
    lb_result_100=Label(window2, text="", font=("courier", 15), borderwidth=2, width=10, relief="solid")
    lb_result_100.place(x=400, y=280)
    lb_line2=Label(window2,text="_______________________________________________",font=("courier",15,"underline"))
    lb_line2.place(x=40,y=310)
    lb_10=Label(window2, text="$10:", font=("courier", 15))
    lb_10.place(x=100,y=360)
    lb_result_10=Label(window2,text="",font=("courier", 15),borderwidth=2,width=10,relief="solid")
    lb_result_10.place(x=400,y=360)
    lb_line3=Label(window2,text="_______________________________________________",font=("courier",15,"underline"))
    lb_line3.place(x=40,y=390)
    lb_1=Label(window2,text="$1:",font=("courier",15))
    lb_1.place(x=100,y=440)
    lb_result_1=Label(window2,text="",font=("courier", 15), borderwidth=2, width=10, relief="solid")
    lb_result_1.place(x=400,y=440)
    window2.mainloop()

btn_continue=Button(window1,text=" Continue ➡️",font=("courier",15,"bold"),bg="green",width=13,command=message_new_window)
btn_continue.place(x=200,y=450)

window1.mainloop()