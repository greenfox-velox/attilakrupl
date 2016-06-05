def namelist(names):
    theList = ""
    nameDict = names
    numOfNames = (len(nameDict))
    if numOfNames == 0:
        return theList
    elif numOfNames == 1:
        theList += nameDict[0].get("name")
    elif numOfNames == 2:
        theList += nameDict[0].get("name")
        theList += " & "
        theList += nameDict[1].get("name")
    else:
        for i in range(numOfNames):
            a = ", "
            b = " & "
            if i < numOfNames - 2:
                theList += (nameDict[i].get("name") + a)
            elif i == numOfNames - 2:
                theList += (nameDict[i].get("name") + b)
            else:
                theList += (nameDict[i].get("name"))
    return theList
    
    
    
    
    
    
print(namelist([{'name': 'Bart'}])) 
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))