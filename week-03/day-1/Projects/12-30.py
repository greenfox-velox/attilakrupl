l = 'python'
print (l[1])

m = 'Apple'
m = m * 4
print (m)

n = 'The result is: '
a = 2
b = 3
n += str(a*b)
print(n)

o = "pneumonoultramicroscopicsilicovolcanoconiosis"
print (len(o))

p1 = [1, 2, 3]
p2 = [4, 5]
print (len(p2) > len(p1))

q = [4, 5, 6, 7]
print (q[2])

r = [54, 23, 66, 12]
print(r[1]+r[2])

s = [1, 2, 3, 8, 5, 6]
s[3] = 4
print (s)

t = [1, 2, 3, 4, 5]
t[2]+= 1
print (t) 

u = 123
if u > 100:
    print ('Hooray!')
    
v = 426
if v % 4 == 0:
    print ('Yeah!')
print ('End of program')

w = 24
out = 0
if w % 2 == 0:
    out+=1
    print(out)
    
x = 'cheese'
if len(x) % 2 == 0:
    print (True)
else:
    print (False)
    
y = 'seasons'
out = 6
if y[0] == y[(len(y)-1)]:
    out *= 2
else:
    out /= 2
print (out)
    
z = 13
if z > 20:
    print ('Less!')
elif z > 10:
    print ('Sweet!')
else:
    print ('More')

aa = [1, 2, 3]
out = 0
if len(aa) > 2:
    out = 10
elif len(aa) == 2:
    out = 2
elif len(aa) == 1:
    out = 1
elif len(aa) == 0:
    out = -1    
print (out)

ab = 123
credits = 100
is_bonus = False
if credits >= 50 and is_bonus == False:
    ab -= 2
elif credits <= 50 and is_bonus == False:
    ab -= 1
print (ab)

ac = 8
time = 120
out = ''
if ac % 2 == 0 and time <= 200:
    out = 'check'
elif time > 200:
    out = 'Time out'
else:
    out = 'Run Forest Run!'
print (out)
 
