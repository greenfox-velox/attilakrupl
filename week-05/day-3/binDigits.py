def countBits(n):
    binary = str(bin(n))
    counter = 0
    for n in binary:
        if "1" in n:
            counter += 1
        else:
            pass
    return counter
    
