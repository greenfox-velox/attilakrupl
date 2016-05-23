# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    f.close()
    
    length = len(result)
    
    text = ""
    
    
    for i in range(length-1,-1, -1):
        text += result[i]
        
    return text
         
    