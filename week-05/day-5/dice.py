import random
def throw_rigged(num):
    dicti = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(num):
        if dicti[6]/(i+1) < 0.22:
            dicti[6] += 1
        elif dicti[6]/(i+1) > 0.22:
            dicti[random.randrange(1,6)] += 1
    print (dicti)
throw_rigged(10000)