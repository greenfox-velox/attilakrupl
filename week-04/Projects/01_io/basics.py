# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result


# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    result = f.readlines()
    x = result[number-1]
    f.close()
    return x.rstrip()

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    x = sentence.split()
    y = []
    for i in x:
        i=i.rstrip('.')
        y.append(i)    
    return y

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    p = ""
    for i in range(len(words)):
        if i < len(words)-1:
            p += words[i] +" "
        else:
            p += words[i] + "."
    return (p)    

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    list1 = []
    for i in string: 
        x = ord(i)
        list1.append(x)
    return list1    
        

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    list1 = ""
    for i in char_codes: 
        x = chr(i)
        list1 += x
    return list1    
    
