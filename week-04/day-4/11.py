from tkinter import *

root = Tk()
w = 600
canvas = Canvas(root, bg='yellow', width=w, height=w)
canvas.pack()

def fractal(x, y, size):
    canvas.create_rectangle(x+size, y, x+size*2, y+size)
    if size <= 5:
        pass
    else:
        s = size // 3
        fractal(x+size, y, s)
        fractal(x+size-s, y+s, s)
        fractal(x+size+s, y+s, s)
        fractal(x+size, y+size-s, s)


fractal(0, 0, 200)
fractal(0, 400, 200)
fractal(200, 200, 200)
fractal(-200, 200, 200)

canvas.create_rectangle(0, 0, w, w)

root.mainloop()