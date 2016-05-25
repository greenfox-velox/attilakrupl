import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=600, height=400, bg="red", cursor="dot")
coord = 0, 0, 180, 180
arc = canvas.create_arc(coord, start=0, extent=180, fill="blue")
canvas.pack()

blackline = canvas.create_line(0,0,200,50)
redline = canvas.create_line(0,100,200, 50, fill="red")
greenBox = canvas.create_rectangle(25,25,130,60, fill="green")

canvas.delete(redline)

root.mainloop()