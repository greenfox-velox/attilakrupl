# create a 300x300 canvas.
# fill it with a checkerboard pattern.

import tkinter
canvWidth=300
canvHeight=300
boxWidth=300/8

def drawToCenter(x,y,color):
    hr = canvas.create_rectangle(x*boxWidth,y*boxWidth,(x+1)*boxWidth,(y+1)*boxWidth, fill=color)
    return hr

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="white")
canvas.pack()

for y in range(8):
    for x in range (8):
        if (x + y) % 2 == 0:
            col = "black"
        else:
            col = "white"
        drawToCenter(x,y,col)

root.mainloop()