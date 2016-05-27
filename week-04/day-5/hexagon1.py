
from tkinter import *
import math
import random

root = Tk()

w = 1100 
canvas = Canvas(root, width = w, height = w)
canvas.pack()
 
def rand_color():
    hexCols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    col = '#'
    for i in range(6):
        col += str(random.choice(hexCols))
    return col

def draw_hexagon(x, y, a):
    canvas.create_polygon([x, y, x + a, y, x + 3*a/2, y + math.sqrt(3)*a/2, x + a, y + math.sqrt(3)*a, x, y + math.sqrt(3)*a, x - a/2, y + math.sqrt(3)*a/2], fill=rand_color(), outline="black")

def draw_fractal(x, y, size):
    draw_hexagon(x, y, size)
    less = size/2
    if size >= 5:
        draw_fractal(x, y, less)
        draw_fractal(x + 3/4*size, y + math.sqrt(3)*size/4 , less)
        draw_fractal(x, y+(math.sqrt(3)*size)/2, less)
    else:
        pass    
    
draw_fractal(250, 10,500)

root.mainloop()