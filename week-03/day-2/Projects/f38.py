numbers = [7, 5, 8, -1, 2]

def own_min(nums):
    a = nums[0]
    for i in nums:
        if i < a:
            a = i
        else:
            pass
    print (a)
    
own_min(numbers)