class Employee:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(f"The name is {self.name}")
        
class Dancer:
    def __init__(self, dance):
        self.dance = dance
        
    def show(self):
        print(f"The dance is {self.dance}")   
         
class DancerEmployee(Employee, Dancer):#if I write dancer employee instead of employee dancer the output will different 
    def __init__(self, name, dance):
        self.dance = dance
        self.name = name
        
o = DancerEmployee("Shiwani", "Kathak")
print(o.name)
print(o.dance)
o.show()