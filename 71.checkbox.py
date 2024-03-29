from tkinter import *

def display():
    if(x.get()==True):
        print("You like it")
    else:
        print("You don't like it.")

window = Tk()
x = BooleanVar()

photo = PhotoImage(file='like.png')
photo = photo.subsample(3)

check_button = Checkbutton(window,
                           text="I like it.",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Arial",20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')

check_button.pack()

window.mainloop()