from tkinter import *
from PIL import Image,ImageTk
#Photo Album
window=Tk()
window.geometry("500x400")
window.title("Photo Album")
pic_1=Image.open("Pic_1 (1).jpg")
pic_1=ImageTk.PhotoImage(pic_1)
pic_2=Image.open("Pic_2 (1).jpg")
pic_2=ImageTk.PhotoImage(pic_2)
pic_3=Image.open("Pic_3 (1).jpg")
pic_3=ImageTk.PhotoImage(pic_3)
pic_4=Image.open("Pic_4 (1).jpg")
pic_4=ImageTk.PhotoImage(pic_4)
pic_5=Image.open("Pic_5 (1).png")
pic_5=ImageTk.PhotoImage(pic_5)
image_list=[pic_1,pic_2,pic_3,pic_4,pic_5]
index=0
lb1=Label(window,image=image_list[index])
lb1.place(x=50,y=50)
#With Slideshow
lb2=Label(window,text="Picture Slideshow",font=("ariel",15,"underline"))
lb2.pack()
def slideshow():
    global index
    index=index+1
    if index==5:
        index=0
    lb1=Label(window, image=image_list[index])
    lb1.place(x=50, y=50)
    lb1.after(5000,slideshow)
slideshow()
#With Buttons
'''def next():
    global index
    index=index+1
    if index==5:
        index=0
    lb1=Label(window, image=image_list[index])
    lb1.place(x=50, y=50)

def back():
    global index
    index=index-1
    if index==-6:
        index=-1
    lb1=Label(window, image=image_list[index])
    lb1.place(x=50, y=50)'''
'''btn1=Button(window,text="Next\n⏭️",command=next)
btn1.place(x=380,y=320)
btn2=Button(window,text="Previous\n    ⏮️️",command=back)
btn2.place(x=100,y=320)'''
window.mainloop()