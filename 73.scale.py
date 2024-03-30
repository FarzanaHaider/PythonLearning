from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")


window = Tk()

hotImage = PhotoImage(file='hot.png')
hotImage=hotImage.subsample(9)
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,
              font=('Consolas',20),
              tickinterval=20,  # numeric interval of the scale
              #showvalue=0, #hide current value
              resolution=5, #increament of slider
              troughcolor='sky blue',
              fg='red',
              bg='black',
              
              )
scale.set((scale['from']-scale['to'])/2+scale['to']) # set current value of slider

scale.pack()

coldImage = PhotoImage(file='cold.png')
coldImage=coldImage.subsample(2)
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()