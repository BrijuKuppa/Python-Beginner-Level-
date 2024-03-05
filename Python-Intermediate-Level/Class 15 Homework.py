#Practice Program-1: Pizza Order
print("Hello! Welcome to Fuquay Pizza!\n\nMenu:\n  Small Pizza: $15\n  Medium Pizza: $20\n  Large Pizza: $25\n------------------\n  Pepperoni for Small Pizza: +$2\n  Pepperoni for Medium Pizza: +$3\n  Pepperoni for Large Pizza: +$3.50\n------------------\n  Extra Cheese: +$1\n\nLets get your order:")
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

print(f"The total cost of the pizza will be: ${price}0")