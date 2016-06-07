from tkinter import *
from map import Map
from character import Character, Boss

root = Tk()
heroImage = "hero-down"
heroPosY = 0
heroPosX = 0
def goDown(event):
    heroPosY += 1
    hero.cr_char(canvas, heroPosX, heroPosY)
    
canvas = Canvas(root, bg='grey', width=720, height=900)
canvas.bind("s", goDown) 
canvas.pack()

map1 = Map()
map1.SetTiles(canvas)
boss = Boss()
boss.cr_char(canvas, 5, 5)
hero = Character(heroImage)
hero.cr_char(canvas, heroPosX, heroPosY)

root.mainloop()



