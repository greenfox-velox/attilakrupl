# 10. The fibonacci sequence is a famous bit of mathematics, and it happens to
# have a recursive definition. The first two values in the sequence are
# 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the
# previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21
# and so on. Define a recursive fibonacci(n) method that returns the nth
# fibonacci number, with n=0 representing the start of the sequence.

def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
        
print (fibo(0))
print (fibo(1))
print (fibo(2))
print (fibo(3))
print (fibo(4))
print (fibo(5))
print (fibo(6))
print (fibo(7))
print (fibo(8))
print (fibo(9))
print (fibo(10))
print (fibo(11))
print (fibo(12))