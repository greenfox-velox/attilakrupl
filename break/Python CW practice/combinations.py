from math import factorial

xs = [100, 76, 56, 44, 33]

def numberOfCombinations(ls, length):
    n = len(ls)
    k = length
    number_of_combintations = factorial(n) / (factorial(k) * factorial(n-k))
    return number_of_combintations

print (numberOfCombinations(xs, 2))

list1 = []


def combination(list, k):
    for i in list    