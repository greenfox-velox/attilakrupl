# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

import tkinter
from random import choice

canvWidth=300
canvHeight=300

def drawToCenter(x, color):
    box = canvas.create_rectangle((canvWidth-x)/2,(canvHeight-x)/2, (canvWidth+x)/2,(canvHeight+x)/2, fill=color)
    return box

def randomColorGenerator():
    digitList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    color = "#"
    for i in range(6):
        r = choice(digitList)
        color += r
    return color

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

for i in range(canvHeight, 0, -10): 
    drawToCenter(i, randomColorGenerator() )

root.mainloop()