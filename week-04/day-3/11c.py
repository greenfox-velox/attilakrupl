import tkinter
from random import choice

canvWidth=300
canvHeight=300
boxSize=10

def drawToCenter(x, y):
    box = canvas.create_rectangle(x,x,y,y, fill="purple")
    return box

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

x = 0
y = 0 
for i in range(7): 
    drawToCenter(x, x+10*i)
    x=x+10*i
    
root.mainloop()