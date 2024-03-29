from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)

window = Tk()
photo = PhotoImage(file='like.png')
photo = photo.subsample(3)      # Adjust the value as needed

button = Button(window,
                text="click me!",
                command = click,
                font=("Comic Sans",30),
                fg="blue",
                bg="gray",
                activeforeground = "green",
                activebackground="gray",
                state=ACTIVE,
                image=photo,
                compound='top')

button.pack()
window.mainloop()
