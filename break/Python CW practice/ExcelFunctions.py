def listOfCriteria(criteria):
    listOfCrit = []
    tags = ''
    numOfTags = 0
    listOfTags = [">","<","="]
    for char in str(criteria):
        if char in listOfTags:
            tags += char
            numOfTags += 1
    word = str(criteria)[numOfTags:len(str(criteria))]   
    if len(tags) > 0:
        listOfCrit.append(tags)
    listOfCrit.append(word)
    return listOfCrit

def checkCriteria(lst, str):
    if lst[0] == str:
        return True
    else:
        return False


def count_if(values,criteria):
    result = 0
    listOfCrit = listOfCriteria(criteria)
    if len(listOfCrit) == 1:
        for value in values:
            if str(value) == str(listOfCrit[0]):
                result +=1
       
    elif checkCriteria(listOfCrit,">="):
        for num in values:
            if num >= int(listOfCrit[1]):
                result +=1
    elif checkCriteria(listOfCrit,"<"):
        for num in values:
            if num < int(listOfCrit[1]):
                result +=1
    elif checkCriteria(listOfCrit,"<="):
        for num in values:
            if num <= int(listOfCrit[1]):
                result +=1
    elif checkCriteria(listOfCrit,"<>"):
        for num in values:
            if num != int(listOfCrit[1]):
                result +=1
    elif checkCriteria(listOfCrit,">"):
        for num in values:
            if num > int(listOfCrit[1]):
                result +=1
    return result
    
    
def sum_if(values,criteria):
    result = 0
    listOfCrit = listOfCriteria(criteria)
    if checkCriteria(listOfCrit,">"):
        for num in values:
            if float(num) > float(listOfCrit[1]):
                result += num
    elif checkCriteria(listOfCrit,">="):
        for num in values:
            if float(num) >= float(listOfCrit[1]):
                result += num
    elif checkCriteria(listOfCrit,"<"):
        for num in values:
            if float(num) < float(listOfCrit[1]):
                result += num
    elif checkCriteria(listOfCrit,"<="):
        for num in values:
            if float(num) <= float(listOfCrit[1]):
                result += num
    elif checkCriteria(listOfCrit,"<>"):
        for num in values:
            if float(num) != float(listOfCrit[1]):
                result += num
    else:
        for num in values:
            if float(num) == float(listOfCrit[0]):
                result += num
    return result
     
def average_if(values,criteria):
    result = 0
    counter = 0
    listOfCrit = listOfCriteria(criteria)
    if checkCriteria(listOfCrit,">"):
        for num in values:
            if float(num) > float(listOfCrit[1]):
                result += float(num)
                counter += 1
    elif checkCriteria(listOfCrit,">="):
        for num in values:
            if float(num) >= float(listOfCrit[1]):
                result += float(num)
                counter += 1
                print (type(counter))
                print (type(result))
    elif checkCriteria(listOfCrit,"<"):
        for num in values:
            if float(num) < float(listOfCrit[1]):
                result += float(num)
                counter += 1
    elif checkCriteria(listOfCrit,"<="):
        for num in values:
            if float(num) <= float(listOfCrit[1]):
                result += float(num)
                counter += 1
    elif checkCriteria(listOfCrit,"<>"):
        for num in values:
            if float(num) != float(listOfCrit[1]):
                result += float(num)
                counter += 1
    else:
        for num in values:
            if float(num) == float(listOfCrit[0]):
                result += float(num)
                counter += 1
    return result / counter

print (count_if([1,3,5,3],'>-1'))
print (count_if(['John','Steve','Rachel','Rebecca','John','John'],'John'))
print (count_if([1,-3.5,5,3],-3.5))
print (sum_if([1,-3.5,5,3],-3.5))
print (average_if([1, 3, 6, -2.6, 10, 11],'>=3'))