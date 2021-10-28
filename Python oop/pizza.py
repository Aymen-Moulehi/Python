from os import system

class Pizza:
    nbePizza = 0
    def __init__(self,mokwnet=[]):
        self.__mokwnet = mokwnet
    @classmethod
    def pizzaVeg(cls):
        return cls(['mrshum','olivies','onion'])
    @classmethod
    def pizzaMar(cls):
        return cls(['mozzirella','saues'])
    def describe(self):
        print(f"i am pizza with {self.__mokwnet}")
    def __str__(self):
        return "i am pizza with {}".format(self.__mokwnet)
    
system('clear')
p1 = Pizza.pizzaMar()
p2 = Pizza.pizzaVeg()
#p1.describe()
#p2.describe()
print(p1)
print(p2)