from tkinter import Tk, Canvas
from map import Map, MapData
from character import Hero
from movement import Movement

def main():
    root = Tk()
    canvas = Canvas(root, bg='grey', width=720, height=900)
    canvas.pack()
    charstats = ("Hero (Level 1) HP: 8/10 | DP: 8 | SP: 6")
    #Create objects:
    my_hero = Hero()
    my_coord = MapData().generate_coordinate_list()
    my_map = Map()
    my_map.SetTiles(canvas, my_coord, my_hero, charstats)
    movements = Movement(my_hero, my_coord, my_map, canvas, charstats)
    
    
    #Add action to buttons: 
    canvas.bind("s", movements.moveTheCharDown)
    canvas.bind("w", movements.moveTheCharUp)
    canvas.bind("a", movements.moveTheCharLeft)
    canvas.bind("d", movements.moveTheCharRight)
    canvas.bind("<Down>", movements.moveTheCharDown)
    canvas.bind("<Up>", movements.moveTheCharUp)
    canvas.bind("<Left>", movements.moveTheCharLeft)
    canvas.bind("<Right>", movements.moveTheCharRight)
    canvas.pack()
    canvas.focus_set()

    root.mainloop()

main()