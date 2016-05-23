# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    
    text = ""
    x = len(result)-1
    i = 0
    while i < x:      
        if result[i] == "\n":
            text += "\n"
            i += 1
        elif result[i] == result[i+1]:
            text += result[i]
            i += 2 
    text += '\n'
 
    return text
