from os import system
from datetime import date

class Teachear:
    __nbeTeachear = 0
    def __init__(self,name,age=0,matieres=[]):
        self.__name = name
        self.__age = age
        self.__matieres = matieres
        Teachear.__nbeTeachear += 1
    def getName(self):
        return self.__name
    def setName(self,newName):
        self.name = newName
    def getAge(self):
        return self.__age
    def setAge(self,newAge):
        self.age = newAge
    def getMatieres(self):
        return self.__matieres
    def addMatieres(self,newMatiere):
        self.__matieres.append(newMatiere)
    def getNbeTeachear(self):
        return Teachear.__nbeTeachear
    #decorators in python pour cree plusieures constrcteur
    @classmethod
    def initWithBirthYear(cls, name , birthYear,matiers):
        return cls(name,date.today().year - birthYear,matiers)
    def describe(self):
        print(f"hello my name is {self.__name} i am {self.__age} years old")
system('clear')
t1 = Teachear('bosa3',55,['algo'])
t2 = Teachear.initWithBirthYear('splinter',1968,['pyhsique','chimie'])
t1.describe()
t2.describe()

