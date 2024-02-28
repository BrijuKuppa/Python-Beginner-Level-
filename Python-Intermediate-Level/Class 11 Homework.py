import firebase_admin
from firebase_admin import credentials,db
#Practice Program-1
'''cred = credentials.Certificate("MyBank Class 11 Homework json.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://mybank-c434e-default-rtdb.firebaseio.com/"})
database=db.reference()'''
#Practice Program-2
'''database.update({"Rahul": "abc@123" , "Sanjay": "vsd@3456"})
data=database.get()
print(data)'''
#Practice Program-3
'''database.update({"Ram": "in@999"})'''
#Practice Program-4
'''print(data["Sanjay"])'''
#Practice Program-5
'''name=input("Enter your bank account name: ")
print(f"Password: {data[name]}")'''
