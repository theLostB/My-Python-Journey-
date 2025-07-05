class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")#We can say that class is a type of blueprint

a = Person()
b = Person()

print(a.name,a.occupation)
a.info()
a.name = "Shubham" #Change
a.occupation = "Accountant" #Change
print(a.name)
print(a.occupation)
a.info()
b.name = "Robert"
b.occupation = "HR"
b.info()