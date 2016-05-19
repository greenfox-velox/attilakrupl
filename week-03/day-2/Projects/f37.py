
numbers = [3, 4, 5, 6, 7]

def even_only(nums):
    a = []
    for i in nums:
        if i % 2 == 0:
            a.append(i)
        else:
            pass
    print (a)
    
even_only(numbers)