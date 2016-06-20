def calculate_age(year_of_birth, current_year):
    if year_of_birth == current_year:
        return "You were born this very year!"
    elif year_of_birth < current_year:
        age = (current_year - year_of_birth)
        if age == 1:
            return "You are " + str(age) + " year old."
        else: 
            return "You are " + str(age) + " years old."
    else: 
        age = (year_of_birth - current_year)
        if age == 1: 
            return "You will be born in " + str(age) + " year."
        else: 
            return "You will be born in " + str(age) + " years."
    
    
print(calculate_age(2012, 2016))
print(calculate_age(2000, 1990))