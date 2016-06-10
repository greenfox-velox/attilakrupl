from tkinter import Tk, Canvas
from gameBoard import Map, Floor
def main():
    root = Tk()
    canvas = Canvas(root, bg='white', width=720, height=900)
    canvas.pack()
    
    map1 = Map()
    map1.drawMap(canvas)
    
    root.mainloop()

main()