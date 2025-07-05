class Employee:
    def __init__(self):
        self.name = "Harry"
#As we know that variables of class is accessible from outside , this type of variable is known as public variable
ac = Employee()
print(ac.name)#this is example of public variable

class Employee1:
    def __init__(self):
        self.__name = "Harry"
#This is private variable class for privating the variable we have to put __ before the variable
aec = Employee1()
#print(aec.name) if we write this than it throws an error for accessing the private variable we have write something like this

print(aec._Employee1__name)
#this is example of private variable

print(ac.__dir__()) #We can see all attribute and methods like this using __dir__
print(aec.__dir__())