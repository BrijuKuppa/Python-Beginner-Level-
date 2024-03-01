#Practice Program-1
'''file=open("Todo","r")
data=file.readlines()
print(f"Data: {data}\n---------------------------")
for i in data:
    print(i)
file.close()'''
#Practice Program-2
'''file=open("Todo","r")
data=file.readlines()
print(f"Data: {data}\n---------------------------")
for i in data:
    print(i,end="")
file.close()'''
#Practice Program-3
'''file=open("Todo2","w")
data=['todo1\n', 'todo2', 'todo3\n', 'todo4', 'todo5\n']
for i in data:
    if i[-1]=="\n":
        file.write(i)
    elif i[-1]!="\n":
        file.write(i+"\n")
file.close()'''