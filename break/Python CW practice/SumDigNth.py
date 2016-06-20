def sumDig_nthTerm(initVal, patternL, nthTerm):
    nth = initVal 
    for i in range(nthTerm-1):
        nth += patternL[i%len(patternL)]
    nth = str(nth)
    x = 0
    for i in range(len(nth)):
        x += int(nth[i])
    return x 

print (sumDig_nthTerm(10, [2, 1, 3], 6))
print (sumDig_nthTerm(10, [2, 2, 5, 8], 6))