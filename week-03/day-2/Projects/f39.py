names = ['Zakarias', 'Hans', 'Otto', 'Ole']

def shortest(strings):
    name = strings[0]
    for i in strings:
        if len(i) < len(name):
            name = i 
        else:
            pass
    print (name)
    
shortest(names)