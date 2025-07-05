class Employee:
    company = "Apple"#Class variable
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
     
    @classmethod
    def changeCompany(cls, newName):
        cls.company = newName
       

e2 = Employee()
e2.changeCompany("Tesla")#If I change the company name which is a class variable , I can't change for all it can only change for e2 like here and it I want to change company name for all that I have to use classMethod
e2.name = "Rohan"
print(Employee.company)#like this 
e2.show()

e1 = Employee()
e1.name = "Harry"
e1.show()