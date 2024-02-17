import urllib.request
import json
import random
from time import sleep
import firebase_admin
from firebase_admin import credentials,db
cred = credentials.Certificate("Class 12.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://class-12-74ed6-default-rtdb.firebaseio.com/"})
database=db.reference()
api="e0b19566bba38f97d53743b5e55c8662"
location=["cary","angier","charlotte","durham","mooresville"]

def weather():
    place2=random.choice(location)
    url=f"https://api.openweathermap.org/data/2.5/weather?q={place2}&APPID={api}"
    response=urllib.request.urlopen(url).read()
    data=json.loads(response)
    temp=data["main"]["temp"]
    temp=round(temp-273.15,2)
    print(f"Location: {place2.title()}, Temperature: {temp}")
    database.update({"Location":place2,"Temprature":temp})
    print(data)

while True:
    weather()
    sleep(1)