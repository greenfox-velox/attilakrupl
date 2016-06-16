def dig_pow(n, p):
    originalNumber = n
    n = list(str(n))
    summary = 0
    power = p
    for i in n:
        summary += int(i)**power
        power += 1
    if summary % originalNumber == 0:
        return int(summary / originalNumber)
    else:
        return -1

print (dig_pow(46288, 3))
