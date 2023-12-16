#Filter Functions
'''num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
output=filter(lambda a:a%10==0,num_list)
print(list(output))'''
#Filtering Names
'''names=["karan", "karvin" , "poovin", "saran", "tharun" , "saranya" , "angela" ,  "sanjith"]
output1=filter(lambda a:len(a)==5,names)
output2=filter(lambda a:a[-1]=="a",names)
print(list(output1))
print(list(output2))'''
#Map Functions
'''names=["karan", "karvin" , "poovin", "saran", "tharun" , "saranya" , "angela" ,  "sanjith"]
output=map(lambda a:a[0],names)
print(list(output))'''
#Mapping Variables
'''names=['Karan.A', 'Karvin.B', 'Poovin.C', 'Saran.D', 'Tharun.E']
output1=map(lambda a:a[0:-2].upper(),names)
print(list(output1))'''
#Sum of Idividual Numbers in the List
'''n1 = [1, 2, 3, 4, 5]
n2 = [4, 5, 6, 7, 8]
output=list(map(lambda a,b:a+b,n1,n2))
print(output)'''
#Filter Numbers Greater Than Equal to 15 Then Multiply Those Numbers by 10
'''numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
output1=list(filter(lambda a:a>=15,numbers))
output2=list(map(lambda b:b*10,output1))
print(output1)
print(output2)'''