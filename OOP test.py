
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