import tkinter

class Character:
    
    def __init__(self, image):
        self.charType = tkinter.PhotoImage(file = "assets/" + image + ".png")
        
    def setPosition(self,x,y):
        self.positionOfChar = [x,y]
           
    def cr_char(self, canv, i, j):
        self.canvas = canv
        self.canvas.create_image(i*72+37,j*72+37,image = self.charType)
    
    def moveChar(self, canv):
        self.cr_char(canv, self.positionOfChar[0], self.positionOfChar[1])

class Boss(Character):
    def __init__(self):
        self.charType = tkinter.PhotoImage(file = "assets/boss.png")
        
    
class Hero(Character):
    
    def __init__(self):
        self.image = "hero-down"
        self.charType = tkinter.PhotoImage(file = "assets/" + self.image + ".png")
                
    def findPosition(self, map1):
        self.position = 0
        for i in range(len(map1)):
            if map1[i].get("c") in (2,5,6):
                self.position = i
            else:
                pass
        return self.position  
 
class Skeleton(Character):
    def __init__(self):
        self.charType = tkinter.PhotoImage(file = "assets/skeleton.png")     

    