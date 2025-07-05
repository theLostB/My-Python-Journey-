#Making a Function
def calculateGmean(a, b):
    mean = (a * b)/(a + b)
    print(mean)
    
def isGreater(a, b):
    if (a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
        
def isLesser(a, b):
    pass
  #pass means that we write this function after sometime this will not give error else this will give error
#Now we created function and we can use this function anywhere


a = 3
b = 5
isGreater(a, b)
calculateGmean(a, b)

c = 9
d = 8
isGreater(c, d)
calculateGmean(c, d)

def average(a, b):
    print("The average is", (a+b)/2)
    
average(4, 5)

def name(fname, nname ="John", lname ="whatson"):
    print("Hello", fname, nname, lname)
    
name("Amy")

def name(fname, nname ="John", lname ="whatson"):
    print("Hello", fname, nname, lname)
    
name("Amy", "Agarwal", "Jain")

def averagea(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum / len(numbers))
    
averagea(9, 5, 6, 8)

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])             

name= [mname="Peter", fname="Jhon", lname="Harry"]
