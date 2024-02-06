class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print("Student - " + str(self.id) + "  Name - " + self.name) 