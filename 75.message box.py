from tkinter import *
from tkinter import messagebox 

def click():
    # messagebox.showinfo(title = 'This is an info message box',message="You are a person")
#    while(True):
#         messagebox.showwarning(title = 'WARNING',message="You have a VIRUS!!!")
    # messagebox.showerror(title = 'ERROR',message="Something went wrong :< ")
    
    # if messagebox.askokcancel(title='ask or cancel',message='Do you want to do the thing'):
    #     print('You did a thing!')
    # else: 
    #     print("You cancel a thing! :< ")

    # if messagebox.askretrycancel(title='ask or cancel',message='Do you want to retry the thing'):
    #     print('You retried a thing!')
    # else: 
    #     print("You cancel a thing! :< ")

    # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
    #     print("I like cake too :) ")
    # else:
    #     print("Why don't you like cake? :(")

    # print(messagebox.askquestion(title='ask question',message='Do you like pie?'))

    answer = messagebox.askyesnocancel(title='Yes no cancel',message='Do you like to code?',icon='warning') # icon can be info, error
    if(answer==True):
        print("You like to code :)")
    elif(answer==False):
        print("Then Why are you watching this?")
    else:
        print("You have dodged the question")

window = Tk()

button = Button(window,command=click,text="click me")
button.pack()

window.mainloop()