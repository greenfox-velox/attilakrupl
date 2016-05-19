# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class pirate:
    
    def __init__(self):
        self.drunk = 0

    def drink_rum(self):
        self.drunk += 1
        
    def hows_goin_mate(self):
        if self.drunk >= 5:
            print ("Arrrr!")
        else:
            print ("Nothin'")
            
Jack_S = pirate()

Jack_S.drink_rum()
Jack_S.hows_goin_mate()
 
Jack_S.drink_rum()       
Jack_S.drink_rum()
Jack_S.hows_goin_mate()

Jack_S.drink_rum()
Jack_S.drink_rum()
Jack_S.drink_rum()
Jack_S.hows_goin_mate()
