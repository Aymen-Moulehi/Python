class Student:
    #class atribut here 
    nbeOfStudent = 0
    def __init__(self,name,age=0,listOfCourses=[]):
        #age=0 default value of age
        #object atribut here
        self.__name = name # i use __name to make this atribut private
        self.__age = age
        self.__listOfCourses = listOfCourses
        #when you create new student nbeOfStudent increment
        Student.nbeOfStudent += 1
    def toString(self):
        #print("name = ",self.name,"\nage = ",self.age,"\nlist of courses = ",self.listOfCourses )
        #the best way is inject element
        print(f"my name is {self.name} i am {self.age} years old and my coureses is {self.listOfCourses}")

    def isOldStudent(self):
        if self.age > 50:
            print("this student is old")
        else:
            print("this student is not old")

s1 = Student('ali',17,[1,2,3])
s2 = Student('ala',17,[1,2,3])

#afficher le nombre d'etudiant
print("le nombre de etudiant: ",Student.nbeOfStudent)
print("le nombre de etudiant: ",s1.nbeOfStudent)

#afficher l'adresse memoire de s1 HEX
print(s1)

#afficher l'adresse memoire de s1 DEC
print(id(s1))

#acces to attribut
print(s1.name)

s1.toString()
s2.isOldStudent()