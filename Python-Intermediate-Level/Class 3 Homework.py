#Different Executions of Time
from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from time import *
window=Tk()
window.geometry("700x300")
window.title("Live Time")
lb1=Label(window,text="Time:",bootstyle=DARK,font=("",15,"underline","bold"))
lb2=Label(window,text="Date:",bootstyle=DARK,font=("",15,"underline","bold"))
lb3=Label(window,text="Zone:",bootstyle=DARK,font=("",15,"underline","bold"))
lb_zone=Label(window,text="",bootstyle=DARK,font=("",30))
lb_time=Label(window,text="",bootstyle=DARK,font=("",30,"underline"))
lb_24=Label(window,text="",bootstyle=DARK,font=("",30))
lb_date=Label(window,text="",bootstyle=DARK,font=("",30))
lb1.pack(pady=10)
lb_time.place(x=105,y=35)
lb_zone.place(x=145,y=245)
lb_24.place(x=105,y=80)
lb2.pack(pady=80)
lb_date.place(x=225,y=160)
lb3.place(x=318,y=210)

def display_time():
    hour = strftime("%I")
    min = strftime("%M")
    sec = strftime("%S")
    ampm = strftime("%p")
    time_zone = strftime("%Z")
    time_USA = f"12 Hour Clock: {hour}:{min}:{sec}-{ampm}"
    lb_time.config(text=time_USA)
    lb_zone.config(text=time_zone)
    lb_time.after(500,display_time)
display_time()

def display_24():
    hour24 = strftime("%H")
    min24 = strftime("%M")
    sec24 = strftime("%S")
    ampm24 = strftime("%p")
    time_zone24 = strftime("%Z")
    time_USA24 = f"24 Hour Clock: {hour24}:{min24}:{sec24}-{ampm24}"
    lb_24.config(text=time_USA24)
    lb_zone.config(text=time_zone24)
    lb_24.after(500,display_24)
display_24()

def display_date():
    year = strftime("%Y")
    month = strftime("%b")
    day = strftime("%a")
    time_zone2 = strftime("%Z")
    time_date = f"{month}/{day}/{year}"
    lb_date.config(text=time_date)
    lb_zone.config(text=time_zone2)
    lb_date.after(500,display_date)
display_date()

window.mainloop()