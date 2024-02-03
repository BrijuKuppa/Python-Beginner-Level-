from tkinter import *
import requests
#Quotes API
window=Tk()
window.title("Quotes")
window_background=PhotoImage(file="background.png")
canva=Canvas(window,width=300,height=414)
canva.pack()
canva.create_image(150,207,image=window_background)
text=canva.create_text(150,207,text=" Quotes:\n  Press the Quote Button to continue.",font=("ariel",15,"bold"),width=250)

def quote_command():
    response=requests.get("https://api.kanye.rest/")
    details=response.json()
    quote=details["quote"]
    canva.itemconfig(text,text=quote)

quote_image=PhotoImage(file="quotes.png")
quote_button=Button(window,image=quote_image,command=quote_command)
quote_button.pack()




window.mainloop()