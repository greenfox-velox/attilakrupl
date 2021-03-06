# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    x = a
    if b > a and b > c:
        x = b
    elif c > a and c > b:
        x = c
    else:
        pass
    return x
    
# Returns the median value of a list given as param
def median(pool):
    pool.sort()
    if len(pool) % 2 == 1: 
        return pool[int((len(pool) - 1) / 2)]
    else:
        return (pool[int((len(pool) - 1) / 2)] + pool[int((len(pool)) / 2)]) / 2 
    
# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiou'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    result = ""
    for char in teve:
        if is_vovel(char):
            result += (char+'v'+char)
        else:
            result += char
    return result