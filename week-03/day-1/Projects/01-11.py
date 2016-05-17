import math

a = 3
a += 10
print(a)

b = 100
b -= 7 
print(b)

c = 44
c *= 2
print(c)

d = 125
d /= 5
print(d)

e = 8
e = e ** 3
print (e)

f = 16
f = math.sqrt(f)
print(f)

g1 = 123
g2 = 345 
result7 = g1 > g2
print ("g1 is greater than g2: ", result7)

h1 = 350
h2 = 200
result8 = 2*h2 > h1
print ("the double of h2 is greater than h1: ", result8)

i1 = 1357988018575474 
result9 = i1 % 11 == 0
print ("i1 has 11 as divisor: ", result9)

j1 = 10
j2 = 3
result10a = j1 > j2**2
result10b = j1 < j2**3
result10 = result10a & result10b
print ("j1 is higher than j2 squared and smaller than j2 cubed: ", result10) 

k = 1521
result11a = k % 3 == 0
result11b = k % 5 == 0
result11 = result11a | result11b
print ("k is dividable by 3 or 5: ", result11)