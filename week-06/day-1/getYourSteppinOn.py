def lenOfInnerList(words):
    listLength = 0
    for i in range(len(words)):
        if i % 2 == 0 and i == 0:
            listLength += len(words[i])
        elif i % 2 == 0 and i > 0:
            listLength += len(words[i]) - 1 
        else:
            pass
    return listLength

def createEmptyList(length):
    emptyList = []
    for i in range(length):
        emptyList.append(' ')
    return emptyList
    
def word_step(s):
    listOfWords = (s.split())
    positionCounter = 0 
    finalList = []
    for i in range(len(listOfWords)):
        listChar = createEmptyList(lenOfInnerList(listOfWords))
        if i % 2 == 0:
            for j in range(len(listOfWords[i])):
                listChar[positionCounter] = listOfWords[i][j]
                if j < len(listOfWords[i]) - 1:
                    positionCounter += 1
                else:
                    pass
            finalList.append(listChar)
        else:
            if i == len(listOfWords) - 1:
                for j in range(1, len(listOfWords[i])):
                    listChar2 = createEmptyList(lenOfInnerList(listOfWords))
                    listChar2[positionCounter] = listOfWords[i][j]
                    finalList.append(listChar2)
            else:
                for j in range(1, len(listOfWords[i]) - 1):
                    listChar3 = createEmptyList(lenOfInnerList(listOfWords))
                    listChar3[positionCounter] = listOfWords[i][j]
                    finalList.append(listChar3)
        
            
    return finalList
            
            
print (word_step('SNAKES SHOE EFFORT TRUMP POTATO'))