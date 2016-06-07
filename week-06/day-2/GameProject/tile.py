import tkinter

class Tile:
    
    def __init__(self, image):
        self.tileType = tkinter.PhotoImage(file = "assets/" + image + ".png")
        
    def cr_image(self, canv, i, j):
        self.canvas = canv
        self.canvas.create_image(i*72+37,j*72+37,image = self.tileType)
        
class Floor(Tile):
    
    def __init__(self, image="floor"):
        self.tileType = tkinter.PhotoImage(file = "assets/" + image + ".png")
        
class Wall(Tile):
    
    def __init__(self, image="wall"):
        self.tileType = tkinter.PhotoImage(file = "assets/" + image + ".png")
    

    