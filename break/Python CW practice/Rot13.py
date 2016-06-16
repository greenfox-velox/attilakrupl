import string
from codecs import encode as _dont_use_this_

def rot13(message):
    message = list(message)
    newMessage = []
    for char in message:
        if ord(char) >= 65 and ord(char) <= 90:
            newMessage.append(chr((((ord(char)+13)-65)%26)+65))
        elif ord(char) >= 97 and ord(char) <= 122:
            newMessage.append(chr((((ord(char)+13)-97)%26)+97))
        else:
            newMessage.append(char)
    return ''.join(newMessage)

print (rot13('ABC2abc'))