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
#         
#     def removeChar(self,canv, direction, value):
#         if direction == "upDown":
#             self.canvas.destroy(self.positionOfChar[0]*72+37,(self.positionOfChar[1]-value)*72+37)
#         
class Boss(Character):
    def __init__(self):
        self.charType = tkinter.PhotoImage(file = "assets/boss.png")
        
    
class Hero(Character):
    
    def __init__(self):
        self.image = "hero-down"
        self.charType = tkinter.PhotoImage(file = "assets/" + self.image + ".png")
                
    def findPosition(self, map):
        self.position = 0
        for i in range(len(map)):
            if map[i].get("h") == 1:
                self.position = i
            else:
                pass
        return self.position  
    
#     def setImage(self, directionValue):
#         if directionValue == 10: 
#             self.image = "hero-down"
#         elif directionValue == -10:
#             self.image = "hero-up"
#         elif directionValue == -1:
#             self.image = "hero-left"
#         elif directionValue == 1:
#             self.image = "hero-right"
            
        
class Skeleton(Character):
    def __init__(self):
        self.charType = tkinter.PhotoImage(file = "assets/skeleton.png")     

    