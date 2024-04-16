from tkinter import *
from Ball import *

import time

BACKGROUND_COLOR = "#000000"

window = Tk()

WIDTH = 1026
HEIGHT = 310

canvas = Canvas(window,bg=BACKGROUND_COLOR,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,2,2,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")
red_ball1 = Ball(canvas,10,10,70,8,2,"red")
blue_ball1 = Ball(canvas,50,50,80,10,20,"blue")
pink_ball1 = Ball(canvas,80,80,150,15,12,"gray")


while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    red_ball1.move()
    blue_ball1.move()
    pink_ball1.move()

    window.update()
    time.sleep(0.01)

window.mainloop()