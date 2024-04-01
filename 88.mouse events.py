from tkinter import *

def dosomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

# window.bind("<Button-1>",dosomething)   # left mouse click
# window.bind("<Button-2>",dosomething)   # mouse scroll wheel
# window.bind("<Button-3>",dosomething)     # right mouse click
# window.bind("<ButtonRelease>",dosomething)  # right mouse click
# window.bind("<Enter>",dosomething)          # enter the window
# window.bind("<Leave>",dosomething)            # leave the window
window.bind("<Motion>",dosomething)           # where the mouse moved

window.mainloop()