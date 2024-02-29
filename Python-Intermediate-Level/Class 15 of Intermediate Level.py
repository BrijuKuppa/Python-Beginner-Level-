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

window.bind('<Return>',add_item)
btn_add=Button(frame2,text="Add to\nTo-Do List",font=("Lucida Fax",10),command=add_btn)
btn_add.grid(row=0,column=0,padx=10)
btn_delete=Button(frame2,text="Delete selected item in\nTo-Do List",font=("Lucida Fax",10),command=delete)
btn_delete.grid(row=0,column=1,padx=10)
btn_save=Button(frame2,text="Save to\nFile",font=("Lucida Fax",10),command=save_to_file)
btn_save.grid(row=0,column=2,padx=10)
btn_show_as_done=Button(frame2,text="Show selected item\nas Done",font=("Lucida Fax",10),command=check)
btn_show_as_done.grid(row=0,column=3,padx=10)
btn_show_as_not_done=Button(frame2,text="Show selected item\nas not Done",font=("Lucida Fax",10),command=uncheck)
btn_show_as_not_done.grid(row=1,column=1,pady=10)
btn_help=Button(frame2,text="How to use\nTo-Do App",font=("Lucida Fax",10),command=uncheck)
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