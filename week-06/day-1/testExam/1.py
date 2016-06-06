# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list
def doubleList(list1):
    list2 = []
    try:
        if type(list1) != list:
            raise TypeError
        for i in list1:
            list2.append(2 * i)
        return list2
    except TypeError:
        return ("Argument provided is not a list")
