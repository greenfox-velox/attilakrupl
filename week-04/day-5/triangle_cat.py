from math import acos
from math import degrees
 
def triangle_type(a, b, c):
    atf = a
    bef1 = b 
    bef2 = c 
    x = 0
    if atf < bef1:
        x = atf
        atf = bef1
        bef1 = x
    else:
        pass
    if atf < bef2:
        x = atf
        atf = bef2
        bef2 = x
    else:
        pass
    if bef1 < bef2:
        x = bef1
        bef1 = bef2
        bef2 = x
    else:
        pass
         
    if bef1 + bef2 <= atf:
        return 0
    else:
        gamma = degrees((acos(((bef1**2)+(bef2**2)-(atf**2))/(2*bef1*bef2))))
        if gamma < 90:
            return 1
        if gamma == 90:
            return 2
        else:
            return 3
         
     
     
print (triangle_type(2,4,6))