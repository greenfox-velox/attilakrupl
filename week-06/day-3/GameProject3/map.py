import character
import tkinter

class Tile:
    
    def __init__(self, image):
        self.tileType = tkinter.PhotoImage(file = "assets/" + image + ".png")
        
    def cr_image(self, canv, i, j):
        self.canvas = canv
        self.canvas.create_image(i*72+37,j*72+37,image = self.tileType)
        
class Floor(Tile):
    
    def __init__(self):
        self.tileType = tkinter.PhotoImage(file = "assets/floor.png")
        
class Wall(Tile):
    
    def __init__(self, image="wall"):
        self.tileType = tkinter.PhotoImage(file = "assets/wall.png")

class MapData:
    
    def __init__(self):
        
        self.game_map = [[2,0,0,1,0,1,0,0,0,0],
                        [0,0,0,1,0,1,0,1,1,0],
                        [0,1,1,1,0,1,0,1,1,0],
                        [0,0,0,0,0,1,3,0,0,0],
                        [1,1,1,1,0,1,1,1,1,0],
                        [0,1,0,1,0,0,0,0,1,4],
                        [0,1,0,1,0,1,1,0,1,0],
                        [0,0,0,4,0,1,1,0,1,0],
                        [0,1,1,1,0,0,4,0,1,0],
                        [0,0,0,1,0,1,1,0,1,0],
                        [0,1,0,1,0,1,0,0,0,0]] 
        
    def generate_coordinate_list(self):
        map_coordinates = []
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                if self.game_map[i][j] == 0:
                    map_coordinates.append({"x":i, "y": j, "t":0, "h":0, "b":0, "s":0})
                elif self.game_map[i][j] == 1:
                    map_coordinates.append({"x":i, "y": j, "t":1, "h":0, "b":0, "s":0})
                elif self.game_map[i][j] == 2:
                    map_coordinates.append({"x":i, "y": j, "t":0, "h":1, "b":0, "s":0})
                elif self.game_map[i][j] == 3:
                    map_coordinates.append({"x":i, "y": j, "t":0, "h":0, "b":1, "s":0})
                elif self.game_map[i][j] == 4:
                    map_coordinates.append({"x":i, "y": j, "t":0, "h":0, "b":0, "s":1})
        return map_coordinates

class Map:
    
    def __init__(self):
         
        self.tiles = 10
        self.floor = Floor()
        self.wall = Wall()
        self.boss = character.Boss()
        self.skeleton = character.Skeleton()
    
    def SetTiles(self, canvas, game_map, hero):
        for j in range(self.tiles+1):
            for i in range(self.tiles):
                if game_map[j*self.tiles+i].get("t")== 0:
                    self.floor.cr_image(canvas,i,j)
                elif game_map[j*self.tiles+i].get("t")== 1:
                    self.wall.cr_image(canvas,i,j)
                else: 
                    pass
                              
                if game_map[j*self.tiles+i].get("b")== 1:
                    self.boss.cr_char(canvas, i, j)
                else:
                    pass
                
                if game_map[j*self.tiles+i].get("s")== 1:
                    self.skeleton.cr_char(canvas, i, j)
                else:
                    pass
                
                if game_map[j*self.tiles+i].get("h")== 1:
                    hero.cr_char(canvas, i, j)
                else:
                    pass
              
                    
        
