# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)
    # print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),entryBox.get())  # will insert a new value
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE,

                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"soup")
listbox.insert(4,"salad")
listbox.insert(5,"burger")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="Delete",command=delete)
deleteButton.pack()

window.mainloop()