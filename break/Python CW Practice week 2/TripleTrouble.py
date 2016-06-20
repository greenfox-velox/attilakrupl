def triple_trouble(one, two, three):
    length = min([len(one), len(two), len(three)])
    result = ''
    for i in range(length):
        result += one[i]
        result += two[i]
        result += three[i]
    return result

print (triple_trouble("aaa","bbb","ccc"))
print (triple_trouble("burn", "reds", "rolls"))
    