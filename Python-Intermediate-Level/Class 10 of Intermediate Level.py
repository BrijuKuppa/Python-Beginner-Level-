#Weather Application
import urllib.request
import json
import random
from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.geometry("500x500")
window.title("Weather in Different Places")
window.config(bg="#8CB9BD")
image=Image.open("weather.jpg")
image=ImageTk.PhotoImage(image)
lb_image=Label(window,image=image,bg="#8CB9BD")
lb_image.place(x=90,y=30)
label_place=Label(window,text="Place:",font=("courier",15,"underline"),bg="#8CB9BD")
label_place.place(x=200,y=230)
place=Label(window,text="[place]",font=("courier",15),bg="#8CB9BD")
place.place(x=190,y=280)
label_weather=Label(window,text="Weather:",font=("courier",15,"underline"),bg="#8CB9BD")
label_weather.place(x=187,y=320)
label_temp=Label(window,text="[temperature]",font=("courier",15),bg="#8CB9BD")
label_temp.place(x=50,y=360)
label_humidity=Label(window,text="Humidity: [humidity]",font=("courier",15),bg="#8CB9BD")
label_humidity.place(x=50,y=400)
api="e0b19566bba38f97d53743b5e55c8662"
location=["cary","angier","charlotte","durham","mooresville"]

def weather():
    place2=random.choice(location)
    url=f"https://api.openweathermap.org/data/2.5/weather?q={place2}&APPID={api}"
    response=urllib.request.urlopen(url).read()
    data=json.loads(response)
    temp=data["main"]["temp"]
    temp=round(temp-273.15,2)
    humidity=data["main"]["humidity"]
    label_temp.config(text=f"Temperature: {temp}")
    label_humidity.config(text=f"Humidity: {humidity}")
    place.config(text=place2.title())
    place.after(1000,weather)
weather()








window.mainloop()