# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

import tkinter
canvWidth=300
canvHeight=300

def drawToCenter(x,y):
    hr = canvas.create_line(x,y,canvHeight/2,canvWidth/2, fill="red")
    return hr

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

drawToCenter(0, 0)
drawToCenter(150, 0)
drawToCenter(22, 34)

root.mainloop()