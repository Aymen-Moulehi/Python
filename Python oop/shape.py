#abstraction in python 
from os import system
from abc import ABC,abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def peremtre(self):
        pass




class Sqare(Shape):
    nbeSqare = 0
    def __init__(self,thol3):
        self.__thol3 = thol3
        Sqare.nbeSqare += 1
    
    def area(self):
        return self.__thol3 * self.__thol3
    
    def peremtre(self):
        return self.__thol3*4

    def __str__(self):
        return f"nombre de sqare total est : {Sqare.nbeSqare}"


system('clear')

s1 = Sqare(5)
s2 = Sqare(3)
print(s1.area())
print(s1)
