def checkHowManyDots(ip):
    numOfDots = 0
    for i in ip:
        if i == ".":
            numOfDots +=1
    return numOfDots
  
def checkIfOctetInRangeAndPositivNumeric(ip):
    try:
        listOfOctets = ip.split('.')
        result = True 
        for i in range(len(listOfOctets)):
            octet = int(listOfOctets[i])
            if octet >= 0 and octet <= 255:
                result += True
            else:
                result += False
        return result 
    except ValueError:
        return False
 
def checkIfOctetDoesntStartWithZero(ip):
    listOfOctets = ip.split('.')
    result = True 
    for i in range(len(listOfOctets)):
        octet = (listOfOctets[i])
        if len(octet) > 1 and octet[0] == '0':
            result += False
        elif i == 0 and listOfOctets[i] == '0':
            result += False
        else:
            result += True
    return result

def checkIfOnlyNumbersAndDots(ip):
    result = True
    for i in ip:
        if i in '.0123456789':
            result = result and True
        else:
            result = result and False
    return result
     
     
def is_valid_IP(strng):
    if checkHowManyDots(strng) == 3 and checkIfOctetInRangeAndPositivNumeric(strng) == 5 and checkIfOctetDoesntStartWithZero(strng) == 5 and checkIfOnlyNumbersAndDots(strng):
        return True
    else:
        return False
  
  
  
print (is_valid_IP('-10.1.56.1'))
