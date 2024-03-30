from tkinter import *

def openfile():
    print("File has been opened!")
def savefile():
    print("File has been opened!")
def cut():
    print("You cut some text")
def copy():
    print("You copied some text")
def paste():
    print("You pasted some text")

window = Tk()

openfileimage=PhotoImage(file="openfolder.png")
openfileimage=openfileimage.subsample(12)
savefileimage=PhotoImage(file="savefolder.png")
savefileimage=savefileimage.subsample(12)
exitfileimage=PhotoImage(file="exitfolder.png")
exitfileimage=exitfileimage.subsample(4)

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0,font=("MV Boli",15))  # added to menubar
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openfile,image=openfileimage,compound='left')
filemenu.add_separator()
filemenu.add_command(label="Save",command=savefile,image=savefileimage,compound='left')
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit,image=exitfileimage,compound='left')

editmenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_separator()
editmenu.add_command(label="Copy",command=copy)
editmenu.add_separator()
editmenu.add_command(label="Paste",command=paste)

window.mainloop()