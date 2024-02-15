import firebase_admin
from firebase_admin import credentials,db
from tkinter import *
from PIL import Image,ImageTk
#Firebase Realtime Database
'''cred = credentials.Certificate("Class 11.json.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://class-11-de3a0-default-rtdb.firebaseio.com/"})
database=db.reference()
database.update({"Grade":["A","B","A","C","D"]})
data=database.get()
print(data)
print(data["Grade"])'''
#Firebase Using GUI With Lights
cred = credentials.Certificate("Class 11.json.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://class-11-de3a0-default-rtdb.firebaseio.com/"})
database=db.reference()
database.update({"Grade":["A","B","A","C","D"]})
data=database.get()
window=Tk()
window.geometry("300x400")
window.title("Light On/Off")
window.config(bg="black")
image1=Image.open("dark on.png")
image0=Image.open("dark off.png")
image1=ImageTk.PhotoImage(image1)
image0=ImageTk.PhotoImage(image0)
lb_0=Label(window,image=image0,bg="black")
lb_0.place(x=70,y=20)

def light_1_0():
    data=database.get()
    data=data["Light"]
    if data==0:
        lb_0.config(image=image0)
    else:
        lb_0.config(image=image1)
    lb_0.after(1000,light_1_0)
light_1_0()










window.mainloop()