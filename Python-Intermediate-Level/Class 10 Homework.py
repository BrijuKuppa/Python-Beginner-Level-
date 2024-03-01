#Practice Program-1
'''numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list=[]
odd_list=[]
output_even=filter(lambda a: a%2==0,numbers)
output_odd=filter(lambda a: a%2==1,numbers)
print(list(output_even))
print(list(output_odd))'''
#Practice Program-2
numbers=[1, 2, 3, 5, 7, 8, 9, 10]
even_numbers=0
odd_numbers=0
for i in numbers:
    if i%2==0:
        even_numbers=even_numbers+1
    else:
        odd_numbers=odd_numbers+1
print(even_numbers)
print(odd_numbers)
#Practice Program-3
'''weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
output=filter(lambda a: a==6,numbers)
print(output)'''