from os import system

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def describe(self):
        print(f"my name is {self.__name} i am {self.__age} years old")






class Man(Person):
    gender = 'Male'
    def __init__(self,name,age,phone,email):
        super().__init__(name,age)
        self.email = email
        self.phone = phone
    def describe(self):
        super().describe()
        print(f"{self.phone} {self.email}")

system('clear')
m1 = Man('Aymen',21,'22222222','moulehiu897@gmail.com')
m1.describe()