from tkinter import *

root = Tk()

canvas = Canvas(root, width = 1200, height=1200)
canvas.pack()

def draw_rectangle(x,y,s):
    canvas.create_rectangle(x, y, x+s, y+s, fill="green")
    
    
def draw_fractal(x,y,size):
    draw_rectangle(x, y, size)
    third = size/3
    if size >=5:
        draw_fractal(x + third, y, third)
        draw_fractal(x + third, y + 2 * third, third)
        draw_fractal(x, y+third, third)
        draw_fractal(x+2*third, y+third, third)
    else:
        pass
    
    
draw_fractal(10, 10, 1100)


root.mainloop()