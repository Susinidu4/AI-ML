from Person import Student, Person

s1 = Student("Nimal", 1000)
s1.details()
s2 = Student("Ajith", 200)
s2.details()

p1 = Person("Winith", 20)
p1.myfunc()

#importing a class
from Person import Person as P
p1 = P("Rajitha", 19)
p1.myfunc()