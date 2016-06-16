
dr = ("+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")    

import re

def generateList(strng):
    listOfDetails = []
    dataList = strng.split('\n')
    phoneNumPattern = re.compile('\d*-\d*-\d*-\d*', re.MULTILINE | re.IGNORECASE | re.DOTALL | re.UNICODE)
    namePattern = re.compile('[<](.*)[>]', re.MULTILINE | re.IGNORECASE | re.DOTALL | re.UNICODE)
    for i in range(len(dataList)-1):
        actualLine = dataList[i]
        singleOnes = []
        singleOnes.append(phoneNumPattern.findall(actualLine))
        singleOnes.append(namePattern.findall(actualLine))
        m = re.search(phoneNumPattern, actualLine)
        actualLine = actualLine[:m.start()] + actualLine[m.end():]
        n = re.search(namePattern, actualLine)
        actualLine = actualLine[:n.start()] + actualLine[n.end():]
        singleOnes.append([actualLine])
        listOfDetails.append(singleOnes)
    return listOfDetails

def tidyTheList(strng):
    listOfData = generateList(strng)
    for i in range(len(listOfData)):
        if len(listOfData[i][2]) > 1:
            listOfData[i][2] = [" ".join(listOfData[i][2])]
        listOfData[i][2] = [(re.sub('[^A-Za-z0-9-.]+', ' ', str(listOfData[i][2]))).strip()]
    return (listOfData) 

def numberOfPhonenumbers(strng,num):
    listOfData = tidyTheList(strng)
    counter = 0
    for i in range(len(listOfData)):
        if num in listOfData[i][0] :
            counter += 1
    return (counter)

def phone(strng, num):
    listOfData = tidyTheList(strng)
    
    numberOfOccurrances = numberOfPhonenumbers(strng, num)
    if numberOfOccurrances > 1:
        return "Error => Too many people: " + num
    elif numberOfOccurrances == 0:
        return "Error => Not found: " + num
    else:
        for i in range(len(listOfData)):
            if num in listOfData[i][0] :
                return "Phone => " + str(listOfData[i][0])[2:-2] + ", Name => " + str(listOfData[i][1])[2:-2] + ", Address => " + str(listOfData[i][2])[2:-2]

    
print (phone(dr, '1-541-754-3010'))
 
    

    
