from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Notepad",
                                          title='Open file okay?',
                                          filetypes=(("text files","*.txt"),
                                          ("all files","*.*")),
                                          )
    
    file = open(filepath,'r')  # to read file
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()