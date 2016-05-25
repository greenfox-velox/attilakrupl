# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

import tkinter
canvWidth=300
canvHeight=300

def drawToCenter(x,y,z,s, col):
    hr = canvas.create_line(x,y,z,s, fill=col)
    return hr

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=canvWidth, height=canvHeight, bg="white")
canvas.pack()
    
def sector1(xrange, yrange):
    for x in range(xrange, yrange, 10):
            drawToCenter(xrange, x, x+10, yrange, "lime")
            drawToCenter( x+10, xrange, yrange, x+10, "purple") 
    return

def sector2():
    for x in range(150, 300, 10):
            drawToCenter(0, x+10, x-140, 300, "lime")
            drawToCenter( x-150, 150, 150, x+10, "purple")
            drawToCenter(150, x-150, x+10, 150, "lime")
            drawToCenter( x, 0, 300, x-140, "purple")  
    return




            
sector1(0,150)
sector1(150,300)
sector2()


        
      



root.mainloop()
