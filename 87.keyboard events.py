from tkinter import *

def dosomething(event):
    # print("You did a thing!")
    print("You pressed: "+event.keysym)
    label.config(text=event.keysym)

window = Tk()

# window.bind("<Return>",dosomething)  #if press enter the function will be called
window.bind("<Key>",dosomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()