def addListOfNumbers(x, n):
    result = 0
    for i in range(x+1,n+1):
        result += i
    return result

def cumulative_triangle(n):
    sum_ = addListOfNumbers(addListOfNumbers(0, n-1),addListOfNumbers(0, n))
    return sum_
 
# print (cumulative_triangle(4))