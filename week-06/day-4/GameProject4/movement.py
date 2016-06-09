from tkinter import PhotoImage

class Movement:

    def __init__(self, my_hero, my_coord, my_map, canvas):
#         self.event = event
        self.my_hero = my_hero
        self.my_coord = my_coord
        self.canvas = canvas
        self.my_map = my_map

    def moveTheCharDown(self,event):
        pos = self.my_hero.findPosition(self.my_coord)
        try:
            if self.my_coord[pos+10].get("t") == 0 and pos+10 < 110:
                self.my_coord[pos]["h"] = 0
                self.my_coord[pos+10]["h"] = 1
                self.my_hero.charType = PhotoImage(file = "assets/hero-down.png")
        except:
            pass
        self.my_map.SetTiles(self.canvas, self.my_coord, self.my_hero)
    
    def moveTheCharUp(self,event):
        pos = self.my_hero.findPosition(self.my_coord)
        try:
            if self.my_coord[pos-10].get("t") == 0 and pos-10 >= 0:
                self.my_coord[pos]["h"] = 0
                self.my_coord[pos-10]["h"] = 1
                self.my_hero.charType = PhotoImage(file = "assets/hero-up.png")
        except:
            pass
        self.my_map.SetTiles(self.canvas, self.my_coord, self.my_hero)
        
    def moveTheCharLeft(self,event):
        pos = self.my_hero.findPosition(self.my_coord)
        try:
            if self.my_coord[pos-1].get("t") == 0 and pos % 10 > 0:
                self.my_coord[pos]["h"] = 0
                self.my_coord[pos-1]["h"] = 1
                self.my_hero.charType = PhotoImage(file = "assets/hero-left.png")
        except:
            pass
        self.my_map.SetTiles(self.canvas, self.my_coord, self.my_hero)
        
    def moveTheCharRight(self,event):
        pos = self.my_hero.findPosition(self.my_coord)
        try:
            if self.my_coord[pos+1].get("t") == 0 and pos % 10 < 9:
                self.my_coord[pos]["h"] = 0
                self.my_coord[pos+1]["h"] = 1
                self.my_hero.charType = PhotoImage(file = "assets/hero-right.png")
        except:
            pass
        self.my_map.SetTiles(self.canvas, self.my_coord, self.my_hero)