from tkinter import *
from PIL import Image,ImageTk
#Practice Program-1: Photo Album
'''window=Tk()
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
pic_6=Image.open("Pic_6 (1).jpg")
pic_6=ImageTk.PhotoImage(pic_6)
pic_7=Image.open("Pic_7 (1).jpg")
pic_7=ImageTk.PhotoImage(pic_7)
pic_8=Image.open("Pic_8 (1).jpg")
pic_8=ImageTk.PhotoImage(pic_8)
pic_9=Image.open("Pic_9 (1).jpg")
pic_9=ImageTk.PhotoImage(pic_9)
pic_10=Image.open("Pic_10 (1).jpg")
pic_10=ImageTk.PhotoImage(pic_10)
image_list=[pic_1,pic_2,pic_3,pic_4,pic_5,pic_6,pic_7,pic_8,pic_9,pic_10]
index=0
lb1=Label(window,image=image_list[index])
lb1.place(x=50,y=50)

def next():
    global index
    index=index+1
    if index==10:
        index=0
    lb1=Label(window, image=image_list[index])
    lb1.place(x=50, y=50)

def back():
    global index
    index=index-1
    if index==-6:
        index=-1
    lb1=Label(window, image=image_list[index])
    lb1.place(x=50, y=50)

btn1=Button(window,text="Next\n⏭️",command=next)
btn1.place(x=380,y=320)
btn2=Button(window,text="Previous\n    ⏮️️",command=back)
btn2.place(x=100,y=320)
window.mainloop()'''
#Practice Program-2: List-String
'''s_list=['a', 'r', 'd', 'u', 'i', 'n', 'o']
blank=""
output=blank.join(s_list)
print(output)
print(output.upper())'''
#Practice Program-3: Sring-List
'''s="arduino"
s_title="ARDUINO"
output=list(s)
print(output)
output_title=list(s_title)
print(output_title)'''
#Random Number Generator
'''import random
random_number=random.randint(1,12)
print(f"Your random number is: {random_number}")'''
#Three Color Variable
'''colors=["red","blue","green"]'''