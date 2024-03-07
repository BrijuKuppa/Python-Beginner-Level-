#Practice Program-1
'''numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list=[]
odd_list=[]
output_even=filter(lambda a: a%2==0,numbers)
output_odd=filter(lambda a: a%2==1,numbers)
print(list(output_even))
print(list(output_odd))'''
#Practice Program-2
'''numbers=[1, 2, 3, 5, 7, 8, 9, 10]
even_numbers=list(filter(lambda a:a%2==0,numbers))
odd_numbers=list(filter(lambda a:a%2!=0,numbers))
even=len(even_numbers)
odd=len(odd_numbers)
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")'''
#Practice Program-3
'''weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
output=list(filter(lambda a: len(a)==6,weekdays))
print(output)'''
#Practice Program-4
'''a=[1, 2, 3]
b=[4, 5, 6]
output=list(map(lambda c,d:c+d,a,b))
print(output)'''