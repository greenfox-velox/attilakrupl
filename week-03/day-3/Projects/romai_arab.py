from pip._vendor.distlib.compat import raw_input
dict_roma = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman_number = raw_input("Enter a roman number:")
def to_roman(input1):
    letters = len(input1)
    current_letter = 0
    arabic = 0
    while current_letter < (letters-1):
        if dict_roma[input1[current_letter]] < dict_roma[input1[current_letter+1]]:
            arabic -= dict_roma[input1[current_letter]]
        else:
            arabic += dict_roma[input1[current_letter]]
        current_letter += 1
    arabic += dict_roma[input1[letters-1]]
    return arabic
print (to_roman(roman_number))
