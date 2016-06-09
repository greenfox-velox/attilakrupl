from tkinter import Tk, Canvas
from map import Map, MapData
from character import Hero
from movement import Movement

def main():
    root = Tk()
    canvas = Canvas(root, bg='grey', width=720, height=900)
    canvas.pack()
    
    #Create objects:
    my_hero = Hero()
    my_coord = MapData().generate_coordinate_list()
    my_map = Map()
    my_map.SetTiles(canvas, my_coord, my_hero)
    movements = Movement(my_hero, my_coord, my_map, canvas)
    
    #Add action to buttons: 
    canvas.bind("s", movements.moveTheCharDown)
    canvas.bind("w", movements.moveTheCharUp)
    canvas.bind("a", movements.moveTheCharLeft)
    canvas.bind("d", movements.moveTheCharRight)
    canvas.pack()
    canvas.focus_set()
    
    root.mainloop()

main()