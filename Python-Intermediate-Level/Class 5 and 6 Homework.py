#Practice Program-1
'''file=open("hm1.txt","r")
data=file.readline()
print(data)
file.close()'''
#Practice Program-2
'''file=open("hm1.txt","r")
data=file.readlines()
lines_list=[]
for i in data:
    lines_list.append(i)
print(lines_list)
file.close()'''
#Practice Program-3
'''file=open("hm1.txt","r")
letters_read5=0
for i in file:
    letters_read5=letters_read5+len(i)
    print(i[0:5])
    break'''
#Practice Program-4
'''file=open("numberlines.txt","w")
for i in range(9199900050,9199900000-1,-1):
    file.write(str(i)+"\n")
file.close()'''
#Practice Program-5
'''file=open("hm1.txt","r")
count=[]
for i in file:
    count=count+i.split(" ")
count_letters=[]
for i in count:
    count_letters.append(len(i))
    if len(i)==12:
        print(i)
max_wordcount=max(count_letters)
print(max_wordcount)
file.close()'''