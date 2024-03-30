from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(initialdir="D:\\PythonLearning",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt",),
                                        ("Text file",".html",),
                                        ("All files",".*",),

                                    ])
    if file is None:
        return
    # filetext = str(text.get(1.0,END))
    filetext = input("Enter some text: ")
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command = savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()