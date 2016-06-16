ones = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "0":"zero"}
tenToTwenty = {"0":"ten", "1":"eleven", "2":"twelve", "3":"thirteen", "4":"fourteen", "5":"fifteen", "6":"sixteen", "7":"seventeen", "8":"eighteen", "9":"nineteen"}
tens = {"2":"twenty", "3":"thirty", "4":"forty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety", "0":""}
powers = {"3":"thousand", "6":"million", "9":"billion", "12":"trillion", "15":"quadrillion", "18":"quintillion", "21":"sextillion", "24":"septillion"}
def splitEveryThird(lst):
    newLst = []
    for i in range(int(len(lst)/3)):
        newLst.append(lst[i*3:i*3+3])
    return newLst
    
def numberToListOfStrings(n):
    lst = []
    n = str(n)
    length = len(n)
    if length % 3 == 1:
        lst.append(n[0])
        n = n[1:length]
        for element in splitEveryThird(n):
            lst.append(element)
    elif length % 3 == 2:
        lst.append(n[0:2])
        n = n[2:length]
        for element in splitEveryThird(n):
            lst.append(element)
    else:
        for element in splitEveryThird(n):
            lst.append(element)
    return lst

def int_to_english(n):
    lst = numberToListOfStrings(n)
    english = []
    for i in range(len(lst)):
        if int(lst[i]) >= 100:
            english.append(ones[lst[i][0]])
            english.append("hundred")
            if int(lst[i][1]) >= 2:
                english.append(tens[lst[i][1]])
            elif int(lst[i][1]) == 1:
                english.append(tenToTwenty[lst[i][2]])
            if int(lst[i][1]) >= 2 or int(lst[i][1]) < 1:
                if int(lst[i][2]) > 0: 
                    english.append(ones[lst[i][2]])
        elif  int(lst[i]) >= 20:
            english.append(tens[str(int(lst[i]))[0]])
            if int(str(int(lst[i]))[1]) > 0:  
                english.append(ones[str(int(lst[i]))[1]])
        elif int(lst[i]) < 20 and int(lst[i]) >= 10:
            english.append(tenToTwenty[str(int(lst[i]))[1]])
        elif int(lst[i]) < 10:
            if int(str(int(lst[i]))[0]) > 0:  
                english.append(ones[str(int(lst[i]))[0]])
        if i < len(lst)-1:
            english.append(powers[str((len(lst)-1-i)*3)])
    english = ' '.join(english)
    return (english)

    
print (int_to_english(6009042968033))