import tkinter

class Tile:
    
    def __init__(self, x, y, type):
        self.position = [x,y]
        self.type = type
        
    def drawTile(self):