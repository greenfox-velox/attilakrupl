# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]


import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

def bindPoints(listOfPoints):
    lengthOfList = len(listOfPoints)
    for i in range(lengthOfList):
        try:
            hr = canvas.create_line(listOfPoints[i][0],listOfPoints[i][1],listOfPoints[i+1][0],listOfPoints[i+1][1], fill="lime")
        except:
            hr = canvas.create_line(listOfPoints[i][0],listOfPoints[i][1],listOfPoints[0][0],listOfPoints[0][1], fill="lime")
    return hr    

bindPoints([[10, 10], [290,  10], [290, 290], [10, 290]])
bindPoints([[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],[120, 100], [85, 130], [50, 100]])
    
root.mainloop()