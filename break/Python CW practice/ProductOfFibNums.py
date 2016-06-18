def productFib(prod):
    result = []
    fibList = [0,1]
    while fibList[-1] < prod/2:
        fibList.append(fibList[-1]+fibList[-2])
    for i in range(1,len(fibList)-1):
        if fibList[i] * fibList[i+1] == prod:
            result.append(fibList[i])
            result.append(int(fibList[i+1]))
            result.append(True)
            break
        elif fibList[i] * fibList[i+1] < prod  and  fibList[i+1] * fibList[i+2] > prod:
            result.append(fibList[i+1])
            result.append(fibList[i+2])
            result.append(False)
            break
    return result
# 
# print (productFib(4895))
# print (productFib(714))
print (productFib(256319508074468182850))