# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
def exToWhy(char):
    if char == "x":
        return "y"
    else:
        return char
        
def readInString(string):
    if len(string) <= 0:
        return ""
    else:
        return exToWhy(string[0]) + readInString(string[1:len(string)])
        
            
print (readInString("Xaver"))     