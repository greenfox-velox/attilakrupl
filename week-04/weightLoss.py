import math
import sys

def lose_weight(gender, weight, duration):
    wlrate = 0
    if gender.upper() == "F":
        wlrate = 0.012
    elif gender.upper() == "M":
        wlrate = 0.015
    else:
        print ("Invalid gender")
        sys.exit()
     
    if duration > 0 :    
        f = math.floor(duration)
    else: 
        print("Invalid duration")
        sys.exit()
        
    if weight > 0:
        result = weight - (weight*wlrate)*f 
        print ('%.1f' % result)
    else:
        print ("Invalid weight") 
        sys.exit()   
    
    
lose_weight("F", 110, 0)