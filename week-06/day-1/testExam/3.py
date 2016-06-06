# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def getSurface(self):
        return 2 * ( self.a * self.b + self.a * self.c + self.b * self.c)
    
    def getVolume(self):
        return (self.a * self.b * self.c)


# tegla = Cuboid(3,4,5)
# 
# print (tegla.getSurface())
# print (tegla.getVolume())