from tkinter import *
import time

WIDTH = 500   # constant height and width
HEIGHT = 300
xvelocity=3
yvelocity=2
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background = PhotoImage(file="background.png")
background_image = canvas.create_image(0,0,image=background,anchor=NW)

photo = PhotoImage(file="ball.png")
photo = photo.subsample(5)
my_image = canvas.create_image(0,0,image=photo,anchor=NW)

image_width = photo.width()
image_height = photo.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xvelocity = -xvelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yvelocity = -yvelocity
    canvas.move(my_image,xvelocity,yvelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()