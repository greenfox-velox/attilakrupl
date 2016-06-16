friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"], ["A5", "X5"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}

import math

def tour(friends, friend_towns, home_to_town_distances):
    distTable1 = home_to_town_distances
    distance = 0
    fTowns2 = {}
    friends2 = friends
    for data in friend_towns:
        fTowns2.update({data[0]:data[1]})
    for friend in friends:
        if friend not in fTowns2:
            friends2.remove(friend)
    print (friends2)
    
    listOfTowns = []
    for friend in friends2:
        for fTown in friend_towns:
            if friend in fTown:
                listOfTowns.append(fTown[1])
    print (listOfTowns)
    
    for i in range(len(listOfTowns)):
        if listOfTowns[i] in distTable1:
            if i == 0 or i == len(listOfTowns):
                distance += distTable1[listOfTowns[i]]
            else:
                distance += (math.sqrt(distTable1[listOfTowns[i]]**2-distTable1[listOfTowns[i-1]]**2))
        else:
            listOfTowns.remove(listOfTowns[i])
    distance += distTable1[listOfTowns[len(listOfTowns)-1]]
    return int(distance)




print(tour(friends1, fTowns1, distTable1))

