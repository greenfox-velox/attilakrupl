# create a function that takes a list and returns a new list with all the elements doubled

def list_doub(*args):
    lista = []
    len_o_li = 0
    for item in args:
        lista.insert(len_o_li, item)
        len_o_li += 1
    print(lista)
    
    doub_lista = []
    iterator = 0
    max_len = len(lista)-1
    while iterator <= max_len:
        doub_lista.append(lista[iterator])
        doub_lista.append(lista[iterator])
        iterator += 1
    return doub_lista
   
print (list_doub("alma", "korte", "szilva", "szolo"))