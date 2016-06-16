import re

def show_me(name):


    if ' ' in name:
        return False
    elif re.search('--', name) is not None:
        return False
    elif re.search('-[a-z]', name) is not None:
        return False
    elif re.search('[a-z][A-Z]', name) is not None:
        return False
    elif re.search('\A-', name) is not None:
        return False
    elif re.search('-$', name) is not None:
        return False
    elif re.search(['^a-zA-Z\-'])is not None:
        return False
    return True
    
    

print (show_me("Francis"))
print (show_me("Jean-Eluard"))
print (show_me("Le Mec"))
print (show_me("Bernard-Henry-Levy"))
print (show_me("Meme Gertrude"))
print (show_me("A-a-a-a----a-a"))
print (show_me("Z-------------"))
print (show_me("Jean-luc"))
print (show_me("Jean--Luc"))
print (show_me("JeanLucPicard"))
print (show_me("-Jean-Luc"))
print (show_me("Jean-Luc-Picard-"))