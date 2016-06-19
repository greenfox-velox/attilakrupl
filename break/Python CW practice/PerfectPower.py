from math import sqrt
def isPP(n):
    print (n)
    result = []
    check = int(sqrt(n))+2
    print (check)
    for i in range(2,check):
        for j in range(2,check):
            if i ** j == n:
                result.append(i)
                result.append(j)
                return result
            elif i ** j > n:
                break
    if not len(result):
        return None
    
print (isPP(8))