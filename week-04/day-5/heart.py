
from tkinter import *
import math
import random
from _tracemalloc import start

root = Tk()

w = 1100 
canvas = Canvas(root, width = w, height = w)
canvas.pack()
 
def draw_heart(x, y, a):
    canvas.create_arc(x, y, x+a, y+a, start=0, extent= 190, style="arc", fill="white", outline="black")
    canvas.create_arc(x+a, y, x+2*a, y+a, start=-10, extent= 190, style="arc", fill="white", outline="black")
    canvas.create_line(x, y+7*a/12, x+a, y+a+a)
    canvas.create_line(x, y,  x+2*a, y)
    canvas.create_line(x, y, x, y+a)

# def draw_fractal(x, y, size):
#     draw_hexagon(x, y, size)
#     less = size/2
#     if size >= 5:
#         draw_fractal(x, y, less)
#         draw_fractal(x + 3/4*size, y + math.sqrt(3)*size/4 , less)
#         draw_fractal(x, y+(math.sqrt(3)*size)/2, less)
#     else:
#         pass    
#     
draw_heart(250, 100, 300)

root.mainloop()