def commonDenom(lst):
    result = 1
    
    a = lst[0]
    b = lst[1]
    c = lst[2]
    for num in a:
        result *= num
        if num in b:
            b.remove(num)
        if num in c:
            c.remove(num)
   
    for num in b: 
        result *= num
        if num in c:
            c.remove(num)
    
    for num in c: 
        result *= num
    
    return result


print (commonDenom([[2, 7], [3], [2, 2, 3]]))