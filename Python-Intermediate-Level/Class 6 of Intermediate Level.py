#Playing with a file.
#Make sure to check file each time you run a piece of code.

#Goal: 9999900000-11. Get these numbers into a file.
'''file=open("numbers.txt","w")
for i in range(9999900010,9999900000-1,-1):
    file.write(str(i)+"\n")
file.close()'''
#Goal: Reading 1 line from a file.
'''file=open("numbers.txt","r")
f_read=file.readline()
print(f_read)'''
#Goal: Converting file line to a list.
'''file=open("numbers.txt","r")
f_read=file.readlines()
numbers_list=[]
for i in f_read:
    f_slice=int(i[:-1])
    numbers_list.append(f_slice)
print(numbers_list)'''
#Goal: Get a message from a user and store it into a file and Text-Speech
'''import pyttsx3
file=open("user_dynamic.txt","w+")
engine=pyttsx3.init()
print("Welcome to File Writer")
while True:
    message=input("Enter text into the File here:")
    file.write(message+"\n")
    user_stop=input("Do you want to save and close the File? Enter 'Yes' or 'No' here:").lower()
    if user_stop=="yes":
        print("File has been closed.")
        break
user_view=input("Do you want to view the File? Enter 'Yes' or 'No' here:").lower()
if user_view=="yes":
    file.seek(0)
    data=file.read()
    print(f"Here is your File:\n\n{data}")
    user_speech=input("Do you want to Text-Speech the File? Enter 'Yes' or 'No' here:").lower()
    if user_speech=="yes":
        engine.say(data)
        engine.runAndWait()
file.close()'''
#Goal: Counting number of lines, characters, and words in a file.
'''f=open("File_Count.txt","r")
letter_count=word_count=line_count=0
for i in f:
    letter_count=letter_count+len(i)
    word_count=word_count+len(i.split(" "))
    line_count=line_count+1
print(f"Letter count: {letter_count}")
print(f"Word count: {word_count}")
print(f"Line count: {line_count}")
f.close()'''