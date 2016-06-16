def Deviders(x):
    lst= []
    for i in range(2,x+1):
        if x % i == 0:
            lst.append(i)
        else:
            pass
        
    return lst 

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

def primTenyezok(a, listA):
    tenyezok = []
    num = a
    i = 0
    while num > 1:
        for i in listA:
            if num % i == 0:
                num = num / i 
                tenyezok.append(i)
            else:
                pass
    return tenyezok   

def commonDenom(lst):
    result = 1
    myList = lst
    for i in range(len(myList)):
        for num in myList[i]:
            result *= num
            for num2 in range(i+1,len(myList)):
                if num in myList[num2]:
                    myList[num2].remove(num) 
    return result

def convertFracts(lst):
    
    listOfPrimesInAll = []
    for listElement in lst:
        primesInN = primTenyezok(listElement[1], CheckPrimes(Deviders(listElement[1])))
        listOfPrimesInAll.append(primesInN)
    
    cD = commonDenom(listOfPrimesInAll) 
    
    result = []
    for i in range(len(lst)):
        result.append([int((lst[i][0])*(cD/(lst[i][1]))), int(cD)])
 
    return result
 
print (convertFracts([[1, 2], [1, 3], [1, 4]]))