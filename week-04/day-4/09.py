# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def readInString(string):
    if len(string) <= 0:
        return ""
    else:
        return string[0] + "*" + readInString(string[1:len(string)])
        
            
print (readInString("Attila"))    