def Deviders(x):
    lst= []
    for i in range(2,x+1):
        if x % i == 0:
            lst.append(i)
        else:
            pass
        
    return lst 

print (Deviders(14))