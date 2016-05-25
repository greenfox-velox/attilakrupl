# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

import tkinter
canvWidth=300
canvHeight=300

def drawToCenter(x,y):
    hr = canvas.create_rectangle(x,y,x+50,y+50, fill="red")
    return hr

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

drawToCenter(45, 10)
drawToCenter(70, 70)
drawToCenter(180, 160)

root.mainloop()