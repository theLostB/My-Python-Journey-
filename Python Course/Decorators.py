def greet(fx):
    def mfx(*args, **kwargs):#Decorators Decorate the function
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this Function")
    return mfx
    
@greet
def hello():
    print("Hello World!")
 
@greet
def sum(a,b):
    print(a+b)
    
def min(a,b):
    print(a-b)
    
hello()
sum(2,9)
greet(min)(8,6)