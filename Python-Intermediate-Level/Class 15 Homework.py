#Practice Program-1: Pizza Order
'''print("Hello! Welcome to Fuquay Pizza!\n\nMenu:\n  Small Pizza: $15\n  Medium Pizza: $20\n  Large Pizza: $25\n------------------\n  Pepperoni for Small Pizza: +$2\n  Pepperoni for Medium Pizza: +$3\n  Pepperoni for Large Pizza: +$3.50\n------------------\n  Extra Cheese: +$1\n\nLets get your order:")
size=input("What size pizza would you like? Choices: Small, Medium, Large. Enter your choice here:").title()
pepperoni=input("Would you like pepperoni on your pizza? Choices: Yes, No. Enter your choice here:").title()
extra_cheese=input("Would you like extra cheese on your pizza? Choices: Yes, No. Enter your choice here:").title()
price=0

if size=="Small":
    price=price+15
elif size=="Medium":
    price=price+20
elif size=="Large":
    price=price+25

if size=="Small" and pepperoni=="Yes":
    price=price+2
elif size=="Medium" and pepperoni=="Yes":
    price=price+3
elif size=="Large" and pepperoni=="Yes":
    price=price+3.5

if extra_cheese=="Yes":
    price=price+1

print(f"The total cost of the pizza will be: ${price}0")'''
#Practice Program-2: Coffee Order
'''print("Welcome to Fuquay Coffee!\nLet's get your order:")
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
    price2=price2+1.00

if milk=="Whole":
    price3=price3+0.50
elif milk=="Skim":
    price3=price3+0.25

price=price1+price2+price3
print(f"Here is your Final Price: ${price}")
print(price1,price2,price3)'''