dict_roma = {1000 : "M", 500: "D", 100 : "C", 50: "L", 10: "X", 5: "V", 1 : "I"}
xxxx_rom = {1: "M"}
xxx_rom = {0:"", 9:"CM", 8:"DCCC", 7:"DCC", 6:"DC", 5:"D", 4:"CD", 3:"CCC", 2:"CC", 1:"CCM"}
xx_rom = {0:"", 9:"XC", 8:"LXXX", 7:"LXX", 6:"LX", 5:"L", 4:"XL", 3:"XXX", 2:"XX", 1:"X"}
x_rom = {0:"", 9:"IX", 8:"VIII", 7:"VII", 6:"VI", 5:"V", 4:"IV", 3:"III", 2:"II", 1:"I"}


def num(n):
    list1 = []
    for i in range(1,5):
        a = (n % 10**i)
        list1.append(int(a/10**(i-1)))
        n = n - a
    return (list1[::-1])

def solution(n):
    listOfValues = num(n)
    roman = ""
    roman += listOfValues[0] * xxxx_rom.get(1)
    roman += xxx_rom.get(listOfValues[1])
    roman += xx_rom.get(listOfValues[2])
    roman += x_rom.get(listOfValues[3])
    return (roman)


solution(1666)