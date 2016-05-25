# create a 300x300 canvas.
# fill it with four different size and color rectangles.

import tkinter
canvWidth=300
canvHeight=300

def drawToCenter(x,y,size, color):
    hr = canvas.create_rectangle(x,y,x+size,y+size, fill=color)
    return hr

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

drawToCenter(45, 10, 35, "red")
drawToCenter(10, 10, 25, "green")
drawToCenter(10, 45, 15, "blue")
drawToCenter(100, 100, 125, "brown")

root.mainloop()