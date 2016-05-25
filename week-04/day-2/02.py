# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

a = canvas.create_line(20,20, 150, 20, fill="red")
b = canvas.create_line(150,20, 150, 150, fill="green")
c = canvas.create_line(150,150, 20, 150, fill="blue")
d = canvas.create_line(20,150, 20, 20, fill="yellow")

root.mainloop()