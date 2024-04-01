from tkinter import *
#To-Do List Application Part-2
window=Tk()
window.geometry("600x600")
window.title("To-Do App")
frame1=Frame(window)
frame1.pack()
list_box=Listbox(frame1,font=("Lucida Fax",15),width=40,height=10,bd=0,highlightthickness=0,selectbackground="grey",activestyle="none")
list_box.pack(side=LEFT)
scroll_bar=Scrollbar(frame1)
scroll_bar.pack(side=RIGHT,fill=BOTH)
list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)
entry_todo=Entry(window,font=("Lucida Fax",15),width=40)
entry_todo.pack(pady=20)
frame2=Frame(window)
frame2.pack(pady=10)
#Button Functions

def add_item(e):
    if entry_todo.get()!="":
        list_box.insert(END, entry_todo.get())
    entry_todo.delete(0,END)

def add_btn():
    if entry_todo.get()!="":
        list_box.insert(END, entry_todo.get())
    entry_todo.delete(0,END)

def delete():
    list_box.delete(ANCHOR)

def save_to_file():
    file=open("ToDo_File","w")
    data=list_box.get(0,END)
    print(data)
    for i in data:
        if i[-1]=="\n":
            file.write(i)
        elif i[-1]!="\n":
            file.write(i + "\n")
    file.close()

def open_form_file():
    file=open("ToDo_File", "r")
    data=file.readlines()
    print(data)
    for i in data:
        list_box.insert(END,i)
    file.close()

def clear():
    list_box.delete(0,END)

def check():
    list_box.itemconfig(list_box.curselection(),fg="green")

def uncheck():
    list_box.itemconfig(list_box.curselection(), fg="black")

def directions():
    window2()

def window2():
    window2 = Toplevel()
    window2.geometry("1400x700")
    window2.title("To-Do App: How to Use")

    directions_title1=Label(window2,text="How to Use:",font=("Lucida Fax",10,"underline","bold"))
    directions_lb2=Label(window2, text="This is an app used to make a list for your priorities. For example, if you want to make list for your chores, homework, and washing the dishes, you can. Here is how to to do that using the UI:", font=("Lucida Fax", 8))
    directions_title2=Label(window2,text="How to Add to Listbox:",font=("Lucida Fax",10,"underline"))
    directions_lb3=Label(window2, text="First, to add something to your list, select (click) and type on the Textbox inbetween the buttons and the Listbox. \nThen, once your done with your list item, press 'enter' on your keyboard, or you can press the 'Add to To-Do List' button to add to the Listbox.", font=("Lucida Fax", 8))
    directions_title3=Label(window2,text="How to Delete from Listbox:",font=("Lucida Fax",10,"underline"))
    directions_lb5=Label(window2,text="First, select (click) the item you want to delete from your Listbox. \nThen, press the 'Delete selected item in To-Do List' button to delete the item.",font=("Lucida Fax",8))
    directions_title4=Label(window2,text="How to Show Selected Item has done in Listbox:",font=("Lucida Fax",10,"underline"))
    directions_lb6=Label(window2,text="First, select (click) the item you want to select. \nThen, press the 'Show selected item as Done', now, it should show the text has green, which means Done.",font=("Lucida Fax",8))
    directions_title5=Label(window2,text="How to Show Selected Item has not done in Listbox:",font=("Lucida Fax",10,"underline"))
    directions_lb7=Label(window2,text="First, select (click) the item you want to show as Not Done. \nMake sure the item has been showed as Done. \nThen, press the 'Show selected item as Not Done' button. \n Now, your Listbox item should be Not Done.",font=("Lucida Fax",8))
    directions_title6=Label(window2,text="How to Save Listbox:",font=("Lucida Fax",10,"underline"))
    directions_lb8=Label(window2,text="First, you need to make sure you have entered items in your Listbox. \nThen, press the 'Save to File' button. Now, your Listbox should be saved.",font=("Lucida Fax",8))
    directions_title7=Label(window2,text="How to Open Saved Listbox:",font=("Lucida Fax",10,"underline"))
    directions_lb9=Label(window2,text="First, if you look at the left corner of the screen you will see a button called 'File'. \nPress that button to see a menu. \n Then, press 'Open' to open the saved Listbox.\n Make sure you have a saved Listbox to use this function.",font=("Lucida Fax",8))
    directions_title8=Label(window2,text="How to Clear Listbox:",font=("Lucida Fax",10,"underline"))
    directions_lb10=Label(window2,text="First, if you look at the left corner of the screen you will see a button called 'File'. \nPress that button to see a menu. \n Then, press 'Clear' to clear your Listbox.",font=("Lucida Fax",8))

    directions_title1.pack(pady=10)
    directions_lb2.pack()
    directions_title2.pack(pady=10)
    directions_lb3.pack()
    directions_title3.pack(pady=10)
    directions_lb5.pack()
    directions_title4.pack(pady=10)
    directions_lb6.pack()
    directions_title5.pack(pady=10)
    directions_lb7.pack()
    directions_title6.pack(pady=10)
    directions_lb8.pack()
    directions_title7.pack(pady=10)
    directions_lb9.pack()
    directions_title8.pack(pady=10)
    directions_lb10.pack()

window.bind('<Return>',add_item)
btn_add=Button(frame2,text="Add to\nTo-Do List",font=("Lucida Fax",10),command=add_btn)
btn_add.grid(row=0,column=0,padx=10)
btn_delete=Button(frame2,text="Delete selected item in\nTo-Do List",font=("Lucida Fax",10),command=delete)
btn_delete.grid(row=0,column=1,padx=10)
btn_save=Button(frame2,text="Save to\nFile",font=("Lucida Fax",10),command=save_to_file)
btn_save.grid(row=0,column=2,padx=10)
btn_show_as_done=Button(frame2,text="Show selected item\nas Done",font=("Lucida Fax",10),command=check)
btn_show_as_done.grid(row=0,column=3,padx=10)
btn_show_as_not_done=Button(frame2,text="Show selected item\nas Not Done",font=("Lucida Fax",10),command=uncheck)
btn_show_as_not_done.grid(row=1,column=1,pady=10)
btn_help=Button(frame2,text="How to use\nTo-Do App",font=("Lucida Fax",10),command=directions)
btn_help.grid(row=1,column=2,padx=15)
#Create a menu bar
def do_something():
    pass
menu_bar = Menu(window)
# Create a File menu
window.config(menu=menu_bar)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Open",command=open_form_file)
file_menu.add_command(label="Clear", command=clear)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.mainloop()