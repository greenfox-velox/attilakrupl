import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

def nato(xrange, yrange, width):
    for i in range(xrange, yrange, width):
        canvas.create_line(i, 150, 150, 150-i, fill="lime")
        canvas.create_line(i, 150, 150, 150+i, fill="lime")
        canvas.create_line(300-i, 150, 150, 150-i, fill="lime")
        canvas.create_line(300-i, 150, 150, 150+i, fill="lime")    
    return

nato(10, 151, 5)

root.mainloop()