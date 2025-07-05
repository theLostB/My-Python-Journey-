class Employee:
    def __init__(self, name):
        self.name = name
        
    def __len__(self):#Magic Methods
        i = 0
        for c in self.name:
            i = i+1
        return i
        
    def __str__(self):#Magic Methods
        return f"The name of Employee is {self.name}"    
        
    def __repr__(self):#Magic Methods
        return f"Employee('{self.name}')"
        
    def __call__(self):#Magic Methods
        print("Hey Iam a call method")
     
a = Employee("harry")
print(len(a)) #Magic method because here we don't need to write __len__ we have to only write len()    
#we can use the len method only when we use __len__ in our class 
print(str(a))#Magic method because here we don't need to write __str__ we have to only write str()
print(repr(a)) #Magic method because here we don't need to write __repr__ we have to only write repr()
a()#Magic method because here we don't need to write __call__ we have to only write class_name()