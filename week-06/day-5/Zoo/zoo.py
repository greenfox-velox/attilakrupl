class Animal(object):
    def __init__(self):
        self.stomach = 0
        self.foodtype = ''
        self.race = ''
        
    def eat(self, food):
        if food != self.foodtype:
            raise Exception ('Bleeeee')
        self.stomach += 1 
        print ('I am a ' + self.race + ' thanks for the ' + self.foodtype)
        
    def poop(self):
        if self.stomach != 0:
            self.stomach -= 1
            print ('My poop smells of ' + self.foodtype)
        else:
            print('LOL did not poop...')

class Okapi(Animal):
    def __init__(self):
        super().__init__()
        self.race = 'okapi'
        self.foodtype = 'shrooms'

class Platypus(Animal):
    def __init__(self):
        super().__init__()
        self.race = 'platypus'
        self.foodtype = 'shrimp'
        
class Zoo(object):
    def __init__(self):
        self.animals = [
                        Platypus(),
                        Platypus(),
                        Okapi()
                        ]
      
        self.food = {
                     "shrimp": 4,
                     "shrooms": 3
                     }
        
    def feed(self):
        for animal in self.animals:
            currentFood = ''
            if type(animal) == Platypus:
                currentFood = 'shrimp'
                animal.eat('shrimp')
                self.food['shrimp'] -= 1
            else:
                currentFood = 'shrooms'
            animal.eat(currentFood)
            self.food[currentFood] -= 1
            animal.poop()
            if self.food[currentFood] == 0:
                raise Exception ("No " + currentFood + " left")
                    
            
budapesti_allat_es_novenykert = Zoo()
budapesti_allat_es_novenykert.feed()
budapesti_allat_es_novenykert.feed()
budapesti_allat_es_novenykert.feed()
print (budapesti_allat_es_novenykert.food)
        
        
# tibor = Okapi()
# tibor.eat('shrooms')
# tibor.poop()
# tibor.poop()
# 
# gerzson = Platypus()
# gerzson.eat('shrimp')
# gerzson.poop()
