class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f' The name of Employee: {self. id} is {self.name}')

e1 = Employee("Rohan das", 400)
e1.showDetails()
e2 = Employee("Harry", 4100)
e2.showDetails()