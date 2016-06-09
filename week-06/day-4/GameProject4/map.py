import character
import tkinter
import stats

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
                    map_coordinates.append({"x":i, "y": j, "c":0})
                elif self.game_map[i][j] == 1:
                    map_coordinates.append({"x":i, "y": j, "c":1})
                elif self.game_map[i][j] == 2:
                    map_coordinates.append({"x":i, "y": j, "c":2})
                elif self.game_map[i][j] == 3:
                    map_coordinates.append({"x":i, "y": j, "c":3})
                elif self.game_map[i][j] == 4:
                    map_coordinates.append({"x":i, "y": j, "c":4})
        return map_coordinates

class Map:
    
    def __init__(self):
         
        self.tiles = 10
        self.floor = Floor()
        self.wall = Wall()
        self.boss = character.Boss()
        self.skeleton = character.Skeleton()
        self.stats = stats.Stats()
            
    def SetTiles(self, canvas, game_map, hero, charstats):
        canvas.delete("all")
        for j in range(self.tiles+1):
            for i in range(self.tiles):
                self.stats.text(charstats,canvas)
                if game_map[j*self.tiles+i].get("c")== 0:
                    self.floor.cr_image(canvas,i,j)
                elif game_map[j*self.tiles+i].get("c")== 1:
                    self.wall.cr_image(canvas,i,j)
                elif game_map[j*self.tiles+i].get("c")== 2:
                    self.floor.cr_image(canvas,i,j)
                    hero.cr_char(canvas, i, j)
                elif game_map[j*self.tiles+i].get("c")== 3:
                    self.floor.cr_image(canvas,i,j)
                    self.boss.cr_char(canvas, i, j)
                elif game_map[j*self.tiles+i].get("c")== 4:
                    self.floor.cr_image(canvas,i,j)
                    self.skeleton.cr_char(canvas, i, j)
                elif game_map[j*self.tiles+i].get("c")== 5:
                    self.floor.cr_image(canvas,i,j)
                    self.boss.cr_char(canvas, i, j)
                    hero.cr_char(canvas, i, j)
                elif game_map[j*self.tiles+i].get("c")== 6:
                    self.floor.cr_image(canvas,i,j)
                    self.skeleton.cr_char(canvas, i, j)
                    hero.cr_char(canvas, i, j)
                else:
                    pass
              
                    
        
