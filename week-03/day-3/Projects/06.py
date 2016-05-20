# create a function that takes a list and returns a new list that is reversed

def list_reverser(*args):
    lista = []
    len_o_li = 0
    for item in args:
        lista.insert(len_o_li, item)
        len_o_li += 1
    print(lista)
    rev_lista = []
    iterator = len(lista)-1
    while iterator >= 0:
        rev_lista.append(lista[iterator])
        iterator -= 1
    return rev_lista
   
print (list_reverser("alma", "korte", "szilva", "szolo"))