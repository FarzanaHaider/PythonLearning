# GUI = Graphical User Interface

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("710x710")
window.title("Farzana Haider")

icon = PhotoImage(file='window.png')
window.iconphoto(True,icon)
window.config(background="#ac8ae3")

window.mainloop()  # place window on computer screen, listen for events
