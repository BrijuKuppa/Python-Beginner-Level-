#Live Time in USA
'''from time import *
while True:
    hour=strftime("%I")
    min=strftime("%M")
    sec=strftime("%S")
    ampm=strftime("%p")
    time_USA=f"{hour}:{min}:{sec}-{ampm}"
    print(time_USA)
    sleep(1)'''
#Live Time in USA in GUI
from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from time import *

window=Tk()
window.geometry("700x300")
window.title("Live Time")
lb1=Label(window,text="Time:",bootstyle=DARK,font=("",19,"underline"))
lb1.place(x=325,y=10)
lb_time=Label(window,text="",bootstyle=DARK,font=("",80))
lb_time.pack(pady=40)
lb_zone=Label(window,text="",bootstyle=DARK,font=("",40))
lb_zone.pack()
def display_time():
    hour = strftime("%I")
    min = strftime("%M")
    sec = strftime("%S")
    ampm = strftime("%p")
    time_zone = strftime("%Z")
    time_USA = f"{hour}:{min}:{sec}-{ampm}"
    print(time_USA)
    lb_time.config(text=time_USA)
    lb_zone.config(text=time_zone)
    lb_time.after(500,display_time)
display_time()

window.mainloop()