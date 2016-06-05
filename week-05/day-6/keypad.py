def presses(phrase):
    list1 =  ("1","a","d","g","j","m","p","t","w"," ","*","#")
    list2 = ("0","b","e","h","k","n","q","u","x")
    list3 = ("c","f","i","l","o","r","v","y")
    list4 = ("2","3","4","5","6","s","8","z")
    list5 = ("7","9")
    
    lowerPhrase = phrase.lower()
    counter = 0
    
    for i in range(len(lowerPhrase)):
        if lowerPhrase[i] in list1:
            counter += 1
        elif lowerPhrase[i] in list2:
            counter += 2
        elif lowerPhrase[i] in list3:
            counter += 3
        elif lowerPhrase[i] in list4:
            counter += 4
        elif lowerPhrase[i] in list5:
            counter += 5
    return counter


print (presses("123456789"))