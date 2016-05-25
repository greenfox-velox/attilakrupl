# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    
    text = ""
    x = len(result)
    i = 0
    char = ""
    
    while i < x:     
        
        if result[i] == "\n":
            text += "\n"
            i += 1
        elif result[i] == " ":
            text += " "
            i += 1
        else: 
            char = chr(ord(result[i])-1)
            text += char
            i += 1 
     
    return text