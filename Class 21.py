#Lambda Function
'''output= lambda a,b,c : f"{a}+{b}+{c}={a+b+c}"
print(output(1,4,4))
output_cubed=lambda d : f"{d} cubed is equaled to {d**3}"
print(output_cubed(73))'''
#Numbers 1,000-10,000 being cubed using Lambda Function
'''for i in range(1000,10001,1000):
    print(output_cubed(i))'''
#Greatest of 3 numbers using Lambda Function
'''output_greatest=lambda a,b,c:f"{a} is greatest" if a>b and a>c else f"{b} is greatest" if b>a and b>c else f"{c} is greatest"
print(output_greatest(76,73.9,90.1))'''
#Checking if number is odd/even using Lambda Function
'''output=lambda a:f"{a} is even" if a%2==0 else f"{a} is odd"
print(output(3))'''