class Employee:
    companyName = "Apple" #Class Variable
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02#Instance Variable
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")
        
emp1 = Employee("Harry")
emp1.raise_amount = 0.04
emp1.companyName = "Google"
emp1.showDetails()