def remove_smallest(numbers):
    eltav = 5
    pos = 0
    array = []
    num1 = numbers
    if len(num1) > 0:
        for i in range(len(num1)):
            if num1[i] < eltav:
                eltav = num1[i]
                pos = i
            else:
                pass
        del num1[pos]
        print (num1)
    else:
        return (array)
        

remove_smallest([1, 2, 1, 1, 5])
