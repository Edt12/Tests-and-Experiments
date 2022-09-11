#Object orientated programming                                                          
"python.suggest.autoImports: false"#disables autoImports for python in thsi vscode file

class Dog:
    def __init__(self,name,age):#whenever create new instance calls this self denotes the object itself
        self.name=name#created an attribute-everytime create new one need to add name as a parameter
        self.age=age
        print(name)
    def add_one(self,x):#always need self in methos
        return x + 1
    def get_age(self):
        return self.age
    def bark(self):#function inside class called method
        print("bark")
    def set_age(self,age):
        self.age=age




d=Dog("ed",12)#creates an instance of type dog called instantiation
d2=Dog("steve",12)
d.set_age(341)
print(d.name)
print(d2.name)
print(d.get_age())
d.bark()#calls method
print(d.add_one(7))
print(type(d))#type tells you what something is e.g string ,integer


#how different classes interact
class Student:
    def __init__(self,name,age,grade):#init has two _ of these
        self.name=name
        self.age=age
        self.grade=grade#0 to 100 

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]#makes students = a blank list

    def add_student(self,student):
        if len(self.students)< self.max_students:
            self.students.append(student)#appends student class made above to a list
            return True
        return False

    def get_average_grade(self):
        value=0
        for student in self.students:#for every student that exists in the course
            value+=student.get_grade()
        return value/len(self.students)




s1=Student("tim",19,95)#makes instance of a class by referncing class then attributes
s2=Student("steve",19,80)
s3=Student("bob",19,20)

course=Course("science",2)
    
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)#references student which is in part 0 of list then asks for name
print(course.get_average_grade())

#inheritance demonstration

class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")#called f string 

    def speak(self):
        print("i dont know what to say")

class Cat(Pet):#to inherit write upper level class name in brackets e.g pet the classes which inherit from it are called derived classes
    def __init__(self, name, age,color):
        super().__init__(name,age)#super means from super class e.g pet init() init tells it to use the superclasses intisialisation then brackets are arguments we want to reference effectively copys initialisation of superclass
        self.color=color
    
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")#called f string also redifined show within this subclass

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fishh(Pet):#fish takes same attributes as pet using pass
    pass

p=Pet("Tim",19)
p.show()
c=Cat("Bill",34,"green")
c.show()
c.speak()
d=Dog("Jill",25)
d.show()
d.speak()
f=Fishh("bubbles",11)
f.speak()

#class attributes
class Person:
    number_of_people=0#Class attribute - an attribute defined for the entire class-same for every instance of the Person class
    def __init__(self,name):
        self.name=name
        Person.number_of_people+=1#counts number of people
    @classmethod
    def number_of_people(cls):#not specific to instence and is instead called on the whole class
        return cls.number_of_people

     
p1=Person("tim")
p2=Person("jill")
Person.number_of_people=8
print(Person.number_of_people)
print(p1.number_of_people)
print(p2.number_of_people)