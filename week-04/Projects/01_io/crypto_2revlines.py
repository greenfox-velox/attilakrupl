# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    f.close()
    
    x = len(result)
    i = 0
    text = ""
    
    while i < x:
        
        rev = result[i]
        i += 1
        line = rev[::-1]
        if line == "\n":
            text += line
        else:    
            text += line.lstrip()
            text += "\n"
           
    fw = open("sajat.txt", 'w')
    fw.write(text)
    fw.close()
    
  
    return text
    
