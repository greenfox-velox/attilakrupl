# create a function that takes a list and returns a new list that is reversed

def list_reverser(*args):
    lista = []
    len_o_li = 0
    for item in args:
        lista.insert(len_o_li, item)
        len_o_li += 1
    
    rev_lista = []
    
    length = len(lista)
    
        
    
    
    
    return lista
   
print (list_reverser("alma", "korte", "szilva", "szolo"))