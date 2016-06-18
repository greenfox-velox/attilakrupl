def alphabet_position(text):
    numCont = []
    for char in text:
        if ord(char.lower()) >= 97 and ord(char.lower()) <= 122:
            numCont.append(str(ord(char.lower())-96))
    return (' '.join(numCont))

print (alphabet_position("The sunset sets at twelve o' clock."))
    
    
    