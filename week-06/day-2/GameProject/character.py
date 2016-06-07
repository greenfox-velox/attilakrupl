import tkinter

class Character:
    
    def __init__(self, image):
        self.charType = tkinter.PhotoImage(file = "assets/" + image + ".png")
        
        
    def cr_char(self, canv, i, j):
        self.canvas = canv
        self.canvas.create_image(i*72+37,j*72+37,image = self.charType)
        
class Boss(Character):
    
    def __init__(self, image="boss"):
        self.charType = tkinter.PhotoImage(file = "assets/" + image + ".png")
    
    
    
    