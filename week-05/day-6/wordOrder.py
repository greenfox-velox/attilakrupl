def order(sentence):
    wordsList = sentence.split()
    newList = []
    s = " "
    for i in range (1, len(wordsList)+1):
        for j in range(len(wordsList)):
            if str(i) in wordsList[j]:
                newList.append(wordsList[j])
            else:
                pass
    sentence = s.join(newList)
    return (sentence)
print (order("is2 Thi1s T4est 3a"))