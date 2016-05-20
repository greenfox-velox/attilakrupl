# Create a function that takes a string and creates a palindrome from it. It should work like this:
# 
# output = create_palindrome('pear')
# 
# print(output) it prints: pearraep

word = input("Please enter a word, and I'm ponna generate a palindrom: ")
def create_palindrom(input1):
    char_num = len(input1)
    while char_num > 0:
        char_num  -= 1
        input1 += (input1[char_num])
    return input1

output = (create_palindrom(word))
print (output)



