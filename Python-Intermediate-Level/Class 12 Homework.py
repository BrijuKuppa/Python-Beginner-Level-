#Coffee Ordering System
print("Welcome to Fuquay Coffee!\nLet's get your order:")
size=input("Here are the Coffee sizes: Small ($2.50), Medium ($3.00), Large ($3.50).\nEnter you Coffee size here:").title()
type1=input("Here are the Coffee types: Espresso ($1.50 extra), Latte or Cappuccino ($2.00 extra), Drip or Americano ($1.00 extra)\nEnter your Coffee type here:").title()
milk=input("Here are the milk types: Whole ($0.50 extra), Skim ($0.25 extra)\nIf you want milk in your Coffee, please enter a type of milk. If you don't want milk in your Coffee, just press Enter to continue. Enter your choice here:").title()
price1=0
price2=0
price3=0

if size=="Small":
    price1=price1+2.50
elif size=="Medium":
    price1=price1+3.00
elif size=="Large":
    price1=price1+3.50

if type1=="Espresso":
    price2=price2+1.50
elif type1=="Latte" or "Cappuccino":
    price2=price2+2.00
elif type1=="Drip" or "Americano":
    price2=price2+2.00

if milk=="Whole":
    price3=price3+0.50
elif milk=="Skim":
    price3=price3+0.25

price=price1+price2+price3
print(f"Here is your Final Price: ${price}")
print(price1,price2,price3)