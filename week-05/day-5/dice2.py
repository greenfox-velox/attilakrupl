import random
def throw_rigged():
    list1 = []
    for i in range(0,100):
        if i < 22:
            list1.append(6)
        else:
            list1.append(random.randrange(1,6))
    i = random.randrange(0,100)
    return list1[i]
