# create a 300x300 canvas.
# draw its diagonals in green.

import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

d1 = canvas.create_line(0,0,300,300, fill="green")
d2 = canvas.create_line(300,0,0,300, fill="green")

root.mainloop()