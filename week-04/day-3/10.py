# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

import tkinter
canvWidth=300
canvHeight=300
lineWidth = 2

def drawToCenter(x):
    
    
    a = canvas.create_line((canvWidth-x)/2,(canvHeight-x)/2,(canvWidth-x)/2,(canvHeight+x)/2, fill="green", width=lineWidth)
    b = canvas.create_line((canvWidth-x)/2,(canvHeight+x)/2,(canvWidth+x)/2,(canvHeight+x)/2, fill="green", width=lineWidth)
    c = canvas.create_line((canvWidth+x)/2,(canvHeight+x)/2,(canvWidth+x)/2,(canvHeight-x)/2, fill="green", width=lineWidth)
    d = canvas.create_line((canvWidth+x)/2,(canvHeight-x)/2,(canvWidth-x)/2,(canvHeight-x)/2, fill="green", width=lineWidth)
    
    return a,b,c,d

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="black")
canvas.pack()

for i in range(20): 
    drawToCenter(10 + 10 * i)


root.mainloop()