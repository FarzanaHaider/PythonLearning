from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='window.png')

label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='white',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')

label.pack()
# label.place(x=0,y=0)

window.mainloop()