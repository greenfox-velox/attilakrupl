from tkinter import Tk, Canvas
from map import Map, MapData
from character import Hero

root = Tk()
canvas = Canvas(root, bg='grey', width=720, height=900)
canvas.pack()

my_coord = MapData().generate_coordinate_list()
my_hero = Hero()
my_map = Map()
my_map.SetTiles(canvas, my_coord, my_hero)

def moveTheCharDown(event):
    global my_coord
    global my_hero
    pos = my_hero.findPosition(my_coord)
    try:
        if my_coord[pos+10].get("t") == 0 and pos+10 < 110:
            my_coord[pos]["h"] = 0
            my_coord[pos+10]["h"] = 1
    except:
        pass
    my_map.SetTiles(canvas, my_coord, my_hero)

def moveTheCharUp(event):
    global my_coord
    global my_hero
    pos = my_hero.findPosition(my_coord)
    try:
        if my_coord[pos-10].get("t") == 0 and pos-10 >= 0:
            my_coord[pos]["h"] = 0
            my_coord[pos-10]["h"] = 1
            my_hero.image = "hero-up"
    except:
        pass
    my_map.SetTiles(canvas, my_coord, my_hero)
    
def moveTheCharLeft(event):
    global my_hero
    global my_coord
    pos = my_hero.findPosition(my_coord)
    try:
        if my_coord[pos-1].get("t") == 0 and pos % 10 > 0:
            my_coord[pos]["h"] = 0
            my_coord[pos-1]["h"] = 1
    except:
        pass
    my_map.SetTiles(canvas, my_coord, my_hero)
    
def moveTheCharRight(event):
    global my_coord
    global my_hero
    pos = my_hero.findPosition(my_coord)
    try:
        if my_coord[pos+1].get("t") == 0 and pos % 10 < 9:
            my_coord[pos]["h"] = 0
            my_coord[pos+1]["h"] = 1
    except:
        pass
    my_map.SetTiles(canvas, my_coord, my_hero)


canvas.bind("s", moveTheCharDown)
canvas.bind("w", moveTheCharUp)
canvas.bind("a", moveTheCharLeft)
canvas.bind("d", moveTheCharRight)
canvas.pack()
canvas.focus_set()
root.mainloop()