def anagramm(string1, string2):
    if (is_contained(string2, string1) 
        and is_contained(string1, string2)): 
        return True
    return False

def is_contained(string1, string2):
    for character in string1:
        if not character in string2:
            return False
    return True

    
