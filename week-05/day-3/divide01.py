# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divisor1(number):
    try: 
        print (10 / number)
    except: 
        print ("fail")
        
        
divisor1(10)
divisor1(0)
divisor1(4)
divisor1("dfd")



    
    