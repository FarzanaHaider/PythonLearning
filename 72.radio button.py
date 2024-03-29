# radio button = similar to checkbox , but you can only select one from a group

from tkinter import *

food = ["pizza","burger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a burger")
    elif(x.get()==2):
        print("You ordered a hotdog")
    else:
        print("huh?")
    
window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
pizzaImage = pizzaImage.subsample(2)
burgerImage = PhotoImage(file='burger.png')
burgerImage = burgerImage.subsample(3)
hotdogImage = PhotoImage(file='hotdog.png')
hotdogImage = hotdogImage.subsample(2)
foodImages = [pizzaImage,burgerImage,hotdogImage]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x, # groups radiobutton together if they share the same variable
                              value=index, # assigns each radiobutton a different value
                              padx=25,
                              font=("Impact",50),
                              image = foodImages[index],
                              compound='left',
                              indicatoron=0, # eliminate cicle indicator
                              width = 400, # sets width of radiobutton
                              command=order, #set command of radiobutton to function
                              )

    radiobutton.pack(anchor=W)

window.mainloop()