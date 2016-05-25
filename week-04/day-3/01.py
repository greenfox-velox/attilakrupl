# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

hr = canvas.create_line(0,150,150,150, fill="red")
vr = canvas.create_line(150,0,150,150, fill="green")

root.mainloop()