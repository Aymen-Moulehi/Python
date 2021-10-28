#static function in python is function thant can not access to class or object attribut
from os import system
class Math:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def pi():
        return 3.14
    

system('clear')

x = Math.add(5,10)
print(x)