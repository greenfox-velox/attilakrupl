
from tkinter import *
import math
import random


root = Tk()

w = 1000
canvas = Canvas(root, width = w, height = w, bg="black")
canvas.pack()

def draw_circle(x, y, a):
    canvas.create_oval(x, y, x+a, y+a, fill="black", outline="gold")

def draw_fractal(x, y, size):
    draw_circle(x, y, size)

    small = size/2.154
    r = small/2
    if small >= 5:
        draw_fractal(x, y+r, small)
        draw_fractal(x+1.85*r, y+0.23*r, small)
        draw_fractal(x+1.6*r, y+2.21*r, small)
        draw_fractal(x+small, y+small, small/6.5)
        draw_fractal(x+1.02*r, y+0.14*r, 0.96*r)
        draw_fractal(x+0.66*r, y+1.5*small, 0.96*r)
        draw_fractal(x+3.33*r, y+0.94*small, 0.96*r)

draw_fractal(50, 50, 900)

root.mainloop()
