# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def sum1(n):
    if n <= 1:
        return 1  
    else:
        return n + sum1(n-1)
    
print (sum1(8))