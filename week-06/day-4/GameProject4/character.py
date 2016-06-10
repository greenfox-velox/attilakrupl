import tkinter
from dice import Dice

class Character:
    
    def __init__(self, image):
        self.charType = tkinter.PhotoImage(file = "assets/" + image + ".png")
        self.level = 0
        self.maxHP = 0
        self.currentHP = 0
        self.DP = 0
        self.SP = 0
        self.name = "character"
         
    def setPosition(self,x,y):
        self.positionOfChar = [x,y]
           
    def cr_char(self, canv, i, j):
        self.canvas = canv
        self.canvas.create_image(i*72+37,j*72+37,image = self.charType)
    
    def moveChar(self, canv):
        self.cr_char(canv, self.positionOfChar[0], self.positionOfChar[1])
        
    def generate_stats_line(self):
        stats_line = self.name + " (Level " + str(self.level) + ") HP: " + str(self.currentHP) + "/" + str(self.maxHP) + " | DP: " + str(self.DP) + " | SP: " + str(self.SP)
        return stats_line
    
    def printStats(self, stat_line, canvas):
        canvas.create_text(350,800, fill="black", font="Arial 15", text=stat_line)
        canvas.update
        
class Hero(Character):
    
    def __init__(self):
        self.image = "hero-down"
        self.charType = tkinter.PhotoImage(file = "assets/" + self.image + ".png")
        self.level = 1
        self.maxHP = 20 + 3 * Dice().d6()
        self.currentHP = self.maxHP
        self.DP = 2 * Dice().d6()
        self.SP = 5 + Dice().d6()
        self.name = "Hero"
    
    def findPosition(self, map1):
        self.position = 0
        for i in range(len(map1)):
            if map1[i].get("c") in (2,5,6):
                self.position = i
            else:
                pass
        return self.position  
    
    def printStats(self, stat_line, canvas):
        canvas.create_text(350,750, fill="black", font="Arial 15", text=stat_line)
        canvas.update
         
class Boss(Character):
    def __init__(self):
        self.charType = tkinter.PhotoImage(file = "assets/boss.png")
        self.level = 1
        self.maxHP = (2 * self.level * Dice().d6()) + Dice().d6()
        self.currentHP = self.maxHP
        self.DP = (self.level / 2 * Dice().d6()) + Dice().d6() / 2
        self.SP = (self.level * Dice().d6()) + self.level  
        self.name = "Boss"

class Skeleton(Character):
    def __init__(self):
        self.charType = tkinter.PhotoImage(file = "assets/skeleton.png")     
        self.level = 1
        self.maxHP = (2 * self.level * Dice().d6())
        self.currentHP = self.maxHP
        self.DP = (self.level / 2 * Dice().d6())
        self.SP = (self.level * Dice().d6())
        self.name = "Skeleton"
    