class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
     
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

#Agar humare pass data alg format me ata hai tb hum class method as alternative constructor ko use krte hai jaise ki yha pr john 1200 manlu string format me arha hai tb hum ye krenge

string = "john-12000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)