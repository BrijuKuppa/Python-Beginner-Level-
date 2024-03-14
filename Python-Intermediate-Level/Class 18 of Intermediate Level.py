#Library Application
class Library:
    def __init__(self,name,book_list):
        self.library_name=name
        self.book_list=book_list
        self.lend_dic={}
        print(f"Welcome to {self.library_name} library.")
    def display(self):
        print(f"Here are all the books in the library:")
        j=1
        for i in self.book_list:
            print(f"{j}. {i}")
            j=j+1
    def borrow_book(self,username,book):
        if book in self.lend_dic.keys():
            print("Uh Oh! The book your asking for is currently not available. Please try again later or look for a different book.")
        else:
            self.lend_dic.update({book:username})
            print(f"Your book ({book}) is checked out. Hope you enjoy the book! ")
    def return_book(self,book):
        self.lend_dic.pop(book)
        print(f"Your book ({book}) has been returned. Thank you!")
    def donate_book(self,book):
        self.book_list.append(book)
        print(f"Your book ({book}) has been donated to the library. Thank you!")

ob1=Library("Coding",["Python Tips","Java Apps ","Java Script Syntax","C Learning","C++ Coding","Lua Programing"])

print("Enter '1' to display all the books in the library.\nEnter '2' to check out a book available in the library.\nEnter '3' to return a book to the library.\nEnter '4' to donate a book for the library.")
while True:
    user_input=input("Enter your purpose here: ")
    if user_input not in ["1","2","3","4"] or "":
        print("Uh Oh! Your response was invalid. Please try again. Tip: Make sure you're not placing a space after your response.")
    elif user_input=="1":
        ob1.display()
    elif user_input=="2":
        book=input("Enter the name of your book to borrow it here: ").title()
        username=input("Enter your name to check out your book here: ").title()
        ob1.borrow_book(username,book)
    elif user_input=="3":
        book=input("Enter the name of your book to return it here: ").title()
        ob1.return_book(book)
    elif user_input=="4":
        book=input("Enter the name of your book you want to donate here: ").title()
        ob1.donate_book(book)
    user_continue_exit=input("Do you want to continue using the app? If so, enter 'c' to continue. If not, enter 'e' to exit. Enter your choice here: ")
    if user_continue_exit=="e":
        print(f"Thank you for spending your time at {ob1.library_name} library.")
        break