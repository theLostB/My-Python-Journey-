class ParentClass:
    def parent_method(self):
        print("This is parent method!")
        
class Childclass(ParentClass):
    
    def parent_method(self):
        print("Harry")
        super().parent_method()
        
    def child_method(self):
        print("This is child method!")
        
child_object = Childclass()
child_object.child_method()
child_object.parent_method()


#Let take another example

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)#Here we take name and id from parent class and then add the language in child class , we use super keywords to access, modify the parent class's method or function
        self.lang = lang

Rohan = Employee("Rohan Das", 420)
Harry = Programmer("Harry", 2345, "Python")
print(Harry.name)
print(Harry.id)
print(Harry.lang)