# create a 300x300 canvas.
# draw a green 10x10 square to its center.

import tkinter
canvWidth=300
canvHeight=300

def drawToCenter(x,y):
    hr = canvas.create_rectangle((canvWidth-x)/2,(canvHeight-y)/2,(canvWidth+x)/2,(canvHeight+y)/2, fill="green")
    return hr

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

drawToCenter(10, 10)

root.mainloop()