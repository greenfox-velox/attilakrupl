af = 123

def double(num):
    return num * 2

print (double(af))



def test(expected, actual):
    if expected == actual:
        print ("check")
    else:
        print ("jaj")
        
        
test(double(2), 4)
test(double(0), 0)
test(double('Bela'), 'BelaBela')
test(double(1.234), 2.468)
test(double("2a"), "barmi")


