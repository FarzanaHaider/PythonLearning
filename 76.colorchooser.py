from tkinter import *
from tkinter import colorchooser #submodule

def click():
    # window.config(bg=colorchooser.askcolor()[1]) #change background color
    color = colorchooser.askcolor() # assign color ta a variable
    colorHex=color[1]               # assign element at index 1 to a variable
    window.config(bg=colorHex)      # change background color

window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()