# print (-5 % 26)
# print (ord("a"))
# print (ord("z"))
# print (ord("A"))
# print (ord("Z"))

def encryptor(key, message):
    mess1 = message    
    encrypted = ""
    b  = key % 26
    for i in range(len(mess1)):
        if ord(mess1[i]) <= 90 and ord(mess1[i]) >= 65:
            if ord(mess1[i]) + b > 90:
                encrypted += chr(((ord(mess1[i]) + b) % 90) + 64)
            else:
                encrypted += chr((ord(mess1[i]) + b))
        elif  ord(mess1[i]) <= 122 and ord(mess1[i]) >= 97:
            if ord(mess1[i]) + b > 122:
                encrypted += chr(((ord(mess1[i]) + b) % 122) + 96)
            else:
                encrypted += chr((ord(mess1[i]) + b))
        else:
            encrypted += mess1[i]
    return encrypted

print (encryptor(13, 'Caesar Cipher'))

# 
# 
# 
#             print (b)
#             print (mess1[i])
#             print (ord(mess1[i]) + b)
#             print ((ord(mess1[i]) + b) % 90)
#             print (chr(((ord(mess1[i]) + b) % 65) + 65))