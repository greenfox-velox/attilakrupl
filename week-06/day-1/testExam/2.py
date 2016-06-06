# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result

def charCount(filename):
    try: 
        string1 = readfile(filename)
        counter1 = 0
        for i in string1:
            if i.lower() == "a":
                counter1 += 1
            else:
                pass
        return counter1
    except FileNotFoundError:
        return 0

            
        