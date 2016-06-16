def remove_smallest(numbers):
#     raise NotImplementedError("TODO: remove_smallest")
    pos = 0
    array = []
    num1 = numbers
    if len(num1) > 0:
        eltav = num1[0]
        for i in range(len(num1)):
            if num1[i] < eltav:
                eltav = num1[i]
                pos = i
        del num1[pos]
        return num1
    else:
        return array
    
    
print (remove_smallest([150, 153, 16, 328, 122, 40, 132, 238]))