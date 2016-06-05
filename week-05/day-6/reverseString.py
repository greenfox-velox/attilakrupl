import re

def reverse_words(str):
    myStringList = re.split(r'(\s+)', str)
    newList = []
    for i in range(len(myStringList)):
        newList.append(myStringList[i][::-1])
    s = ""
    return s.join(newList)
    
print(reverse_words('This is an example!'))