def anagram(string1, string2):
    if len(string1) == len(string2):
        list1 = list(string1.lower())
        list2 = list(string2.lower())
        if sorted(list1) == sorted(list2):
            return True
        else:
            return False
    else:
        return False
    
def count_letters(string3):
    letter_dict = {}
    case_string = string3.lower()
    for i in case_string:
        if i not in letter_dict:
            letter_dict[i] = 1
        else: 
            letter_dict[i] += 1
    return letter_dict

# print(count_letters("what is Your name?"))
         
     
