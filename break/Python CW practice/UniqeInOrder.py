def unique_in_order(iterable):
    new = []
    for i in range(len(iterable)):
        if i == 0:
            new.append(iterable[i])
        elif iterable[i] == iterable[i-1]:
            pass
        else:
            new.append(iterable[i])
    return new
print (unique_in_order('AAAABBBCCDAABBB'))    


