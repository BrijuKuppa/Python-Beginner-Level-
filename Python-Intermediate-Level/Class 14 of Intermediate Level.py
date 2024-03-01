from tkinter import *
#To-Do List Application Part-1
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
btn_add=Button(frame2,text="Add to\nTo-Do List",font=("Lucida Fax",10))
btn_add.grid(row=0,column=0,padx=10)
btn_delete=Button(frame2,text="Delete selected item in\nTo-Do List",font=("Lucida Fax",10))
btn_delete.grid(row=0,column=1,padx=10)
btn_save=Button(frame2,text="Save to\nFile",font=("Lucida Fax",10))
btn_save.grid(row=0,column=2,padx=10)
btn_show_as_done=Button(frame2,text="Show selected item\nas Done",font=("Lucida Fax",10))
btn_show_as_done.grid(row=0,column=3,padx=10)
# Create a menu bar
def do_something():
    pass
menu_bar = Menu(window)
# Create a File menu
window.config(menu=menu_bar)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New", command=do_something)
file_menu.add_command(label="Open", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.mainloop()