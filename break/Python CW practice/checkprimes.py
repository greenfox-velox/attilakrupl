def CheckPrimes(lst):
    newLst = []
    for number in lst:
        prime = True
        for divider in range(2,number):    
            if number % divider == 0:
                prime = False
        if prime == True: 
            newLst.append(number)
    return newLst


print (CheckPrimes([2, 7, 14]))