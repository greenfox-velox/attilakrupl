students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

def sugar(dicti):
    candie = 0
    for stud in dicti:
        if stud['age'] < 10:
            candie += stud['candies']
        else:
            pass
    return candie

print (sugar(students))