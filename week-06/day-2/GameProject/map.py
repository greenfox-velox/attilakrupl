from tkinter import *
from tile import Tile, Wall
from map_data import MapData

class Map:
    
    def __init__(self):
        self.game_map = MapData().generate_coordinate_list() 
        self.tiles = 10
        self.floor = Tile("floor")
        self.wall = Wall()
    
    def SetTiles(self, canvas):
        for j in range(self.tiles+1):
            for i in range(self.tiles):
                if self.game_map[j*self.tiles+i].get("t")== 0:
                    self.floor.cr_image(canvas,i,j)
                elif self.game_map[j*self.tiles+i].get("t")== 1:
                    self.wall.cr_image(canvas,i,j)
        
    
    