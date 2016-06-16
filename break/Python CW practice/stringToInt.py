def my_parse_int(string):
    listOfNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    newString = ''
    noWhitespace = string.strip()
    for character in noWhitespace:
        if character in listOfNumbers:
            newString += character
        else:
            return "NaN"
    return int(newString)

print (my_parse_int("2 1"))