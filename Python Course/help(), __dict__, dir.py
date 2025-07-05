x = [1, 2, 3]
print(dir(x))#dir function use to print the list of all the class, methods and attributes of anything
print("\n", x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
        
p = Person("Harry", 14)
print("\n", p.__dict__)#__dict__ attribute use to return a dictionary representation of an object's attribute 

print("\n", help(p))#Help method print the all documentation of an object