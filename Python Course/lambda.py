#def double(x):
#    return x*2 #We can write function like this also but for small function we can use lambda function , and lambda function is written in one line also

double = lambda x: x*2 
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2#This is how we can write it, at first we write function name than = than lambda than variable which we use in our function than : than we write the function what we want to write 
print(double(5))
print(cube(7))
print(avg(5,8))