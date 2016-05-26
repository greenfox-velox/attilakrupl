# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def replaceWithSpace(char):
    if char == "x":
        return ""
    else:
        return char
        
def readInString(string):
    if len(string) <= 0:
        return ""
    else:
        return replaceWithSpace(string[0]) + readInString(string[1:len(string)])
        
            
print (readInString("xoxoxoxox"))    