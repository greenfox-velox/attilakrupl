from tkinter import *
from math import sqrt

root = Tk()

w = 1000 
canvas = Canvas(root, width = w, height = w)
canvas.pack()

def draw_triangle(x, y, s):
    canvas.create_polygon([x, y, x+s, y, x + s/2, y + (s * sqrt(3)/ 2) ], fill="white", outline="black")
    
    
def draw_fractal(x, y, size):
    draw_triangle(x, y, size)
    less = size/2
    if size >= 10:
        draw_fractal(x, y, less)
        draw_fractal(x+less,y, less)
        draw_fractal(x+less/2, y+less*sqrt(3)/ 2, less)
    else:
        pass




draw_fractal(10, 10, 900)

root.mainloop()