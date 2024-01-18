#File Handling
#Steps to Read, Write, Append, r+, w+, a+, and x to a File:

#Note: Uncomment one mode at a time to use. Make sure to check the file each time you run the code.

#Create a File
'''File Name is Prototype_File.txt'''

#Open the File
'''file=open("Prototype_File.txt","r")'''

#Read the File
'''file_read=file.read()
print(file_read)
file.close()'''

#Write the File
'''file=open("Prototype_File.txt","w")
file.write("Coding is very useful for software engineering.")
file.close()
file_read=open("Prototype_File.txt","r")
data=file_read.read()
print(f"Data Writen: {data}")
file.close()'''

#Append/Add to the File
'''file=open("Prototype_File.txt","a")
file.write("\nAlso, coding has different types of languages as well.")
file.close()'''

#Read and Write/r+ to a File
'''file=open("Prototype_File.txt","r+")
file.seek(0)
data=file.read()
print(data)
file.write("One langauge of coding is Python.")
file.close()'''

#Write and Read/w+ to a File
'''file=open("Prototype_File2.txt","w+")
file.write("Another langauge of coding is Java.")
file.close()'''

#Append and Read/a+ to a File
'''file=open("Prototype_File3.txt","a+")
file.write("\nAnother language of coding is JavaScript.")
file.seek(0)
data=file.read()
print(data)
file.close()'''

#Exclusively/x Create File
'''file=open("Prototype_File4.txt","x")'''

#Close the File
'''file.close()'''