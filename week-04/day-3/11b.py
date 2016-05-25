import tkinter
from random import choice

canvWidth=300
canvHeight=300
boxSize=10
numOfBoxes = int(canvHeight/boxSize)

def drawToCenter(x):
    box = canvas.create_rectangle(0+x, 0+x,0+x+boxSize, 0+x+boxSize, fill="purple")
    return box

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

for i in range(numOfBoxes): 
    drawToCenter(i*boxSize)

root.mainloop()