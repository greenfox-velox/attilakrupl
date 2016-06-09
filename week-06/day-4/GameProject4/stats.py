from tkinter import Canvas

class Stats:
    
    def text(self, charstats, canvas):
        canvas.create_text(350,820,fill="black", font="Arial 15", text=charstats)
        canvas.update