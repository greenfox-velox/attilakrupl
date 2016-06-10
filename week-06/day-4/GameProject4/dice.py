from random import randint

class Dice: 

    def d6(self):
        self.value = randint(1,6)
        return self.value