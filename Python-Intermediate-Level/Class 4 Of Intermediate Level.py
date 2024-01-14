#Data Types

#List Data Type: Lists Of Data That's Modifiable
'''animals=["monkey","bear","bird","panda"]
animals[2]="gorilla"
print(animals)'''
#Tuple Data Type: Lists Of Data That's Not Modifiable
'''animals=("monkey","bear","bird","panda")
print(animals)'''
#Dictionary Data Type: Data With Key Valves/Names
'''animals={"birds":"Peacock","bears":"Brown Bear"}
print(animals["birds"])
bank_acn={"lim":12345, "sam":3456}
bank_acn["caryn"]="999"
print(bank_acn)
bank_balance={"lim":5000,"sam":5000}
bank_balance["lim"]=bank_balance["lim"]+2000
print(f"Bank Balance: ${bank_balance['lim']}")
bank_balance["sam"]=bank_balance["sam"]-1000
print(f"Bank Balance: ${bank_balance['sam']}")'''
#Password Checker With Dictionary Data
'''bank_acn={"Lim":12345, "Sam":3456}
input_username=input("Enter Your Bank Account Username:").title()
input_password=int(input("Enter Your Bank Account Password:"))
if input_username not in bank_acn.keys():
    print("Incorrect information entered.")
elif input_password==bank_acn[input_username]:
    print(f"{input_username}, you have been verified.")
else:
    print("Incorrect information entered.")'''