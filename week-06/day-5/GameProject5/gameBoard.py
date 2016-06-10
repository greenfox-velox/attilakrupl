import tkinter

class gameElement(object):

    def drawElement(self, canvas, x, y):
        canvas.create_image(x*72+37,y*72+37,image = self.TileImage)
        
class Floor(gameElement):
    
    def __init__(self):
        super().__init__()
        self.TileImage = tkinter.PhotoImage(file = "assets/floor.png")
        self.accessible = True
        
class Wall(gameElement):
    
    def __init__(self):
        super().__init__()
        self.TileImage = tkinter.PhotoImage(file = "assets/wall.png")
        self.accessible = False
        
class MapData:
    
    def __init__(self):
        
        self.game_map = [[0,0,0,1,0,1,0,0,0,0],
                        [0,0,0,1,0,1,0,1,1,0],
                        [0,1,1,1,0,1,0,1,1,0],
                        [0,0,0,0,0,1,0,0,0,0],
                        [1,1,1,1,0,1,1,1,1,0],
                        [0,1,0,1,0,0,0,0,1,0],
                        [0,1,0,1,0,1,1,0,0,0],
                        [0,0,0,0,0,1,1,0,1,0],
                        [0,1,1,1,0,0,0,0,1,0],
                        [0,0,0,1,0,1,1,0,1,0],
                        ] 
        
    def generate_coordinate_list(self):
        map_coordinates = []
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                if self.game_map[i][j] == 0:
                    map_coordinates.append({"x":i, "y": j, "c":0})
                elif self.game_map[i][j] == 1:
                    map_coordinates.append({"x":i, "y": j, "c":1})
        return map_coordinates
    
class Map:
    
    def __init__(self):
        self.data = MapData().generate_coordinate_list()
        self.wall = Wall()
        self.floor = Floor()
    def drawMap(self, canvas):
        for i in range(len(self.data)):
            if self.data[i].get('c') == 0:
                self.floor.drawElement(canvas,self.data[i].get('y'),self.data[i].get('x'))
            else:
                self.wall.drawElement(canvas, self.data[i].get('y'),self.data[i].get('x'))
                
    