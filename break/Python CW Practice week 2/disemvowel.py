def disemvowel(string):
    newString = ''
    for char in string:
        print (char)
        if char.lower() in "aeiou":
            newString += ''
        else:
            newString += char
    return newString

print (disemvowel("This website is for losers LOL!"))