numbers = [3, 4, 5, 6, 7]

def revert(li):
    a = []
    b = len(li)
    while b > 0:
        b -= 1
        a.append(li[b])
    print (a)
revert(numbers)
        