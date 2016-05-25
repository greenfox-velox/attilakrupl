# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

import tkinter
canvWidth=300
canvHeight=300

def drawToCenter(x,y):
    hr = canvas.create_line(x,y,canvHeight/2,canvWidth/2, fill="red")
    return hr

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="white")
canvas.pack()

for x in range(0, 301, 20):
    for y in range (0, 301, 300):
        drawToCenter(x, y)
        drawToCenter(y, x)



root.mainloop()