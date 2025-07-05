
a = "1"
b = "2"
print(a + b)

c = 1
d = 2
print(c + d)

e = "1"
f = "2"
print(int(e) + int(f))
print(type(a))
print(type(c))
a = (input('Write first number: '))
b = (input('Write second number: '))
print(a+b)
a = int((input('Write first number: ')))
b = int((input('Write second number: ')))
print(a+b)
a = (input('Write first number: '))
b = (input('Write second number: '))
print(int(a)+int(b))
apple = ''' hello my name is
Rishaank Gupta 
I am student of 
Class-7 '''
print(apple)

'''
apple2 = ' hello my name is
Rishaank Gupta 
I am student of 
Class-7 '
print(apple2)
this code gives a error
'''
e = "element"
print(e[0])
print(e[1])
print(e[2])
print(e[3])
print(e[4])
print(e[5])
print(e[6])
#Like this we get element of string one by one
print("Lets use for loop/n")
for character in apple: 
      print(character)
      
names = "harry,rishaank,shubham"
print(names[0:5])
print(names[2:5])
print(names[0:-3])
print(names[-3:-1])
print(len(names))

fruit = "Mango"
len1 = len(fruit)
print("The length of Mango is", len1)

nm = "harry"
print(nm[-4: -2])

a = "Rishaank"#strings
print(len(a))#are
print(a.upper())#immutable
print(a.lower())

#rstrip
r = "Rishaank!!!!!!!!!"
print(r)
print(r.rstrip("!"))

a = "!!!!!!!!!Rishaank!!!!!!!!!"
print(a)
print(r.rstrip("!"))

ar = "!!!!!!!!!Rishaank"
print(ar)
print(r.rstrip("!"))

#replace
#This will replace the character
ra = "Rishaank"
print(ra)
print(ra.replace("Rishaank", "Gupta"))

#Split
#This will split and make the dictionary
r1 = "Rishaank Gupta"
print(r1.split(" "))

#Capitalize
#This will convert small to capital letter of sentence...
capitalizeheading = "i am the best"
print(capitalizeheading.capitalize())
capital = "i am the bESt"#if you make mistake and write any letter capital in sentence it will correct that and makr 1st sentence of letter capital and remaining character to small...
print(capital.capitalize())

#Center()
str2 = "Welcome To Console"
print(len(str2))
print(str2.center(50))
print(len(str2.center(50)))

#Count()
#Simply this  method us eto count how many times the given word is repeated
aar = "Rishaank Rishaank"
print(aar.count("Rishaank"))

#endswith
arar = "Welcome to console"
print(arar.endswith("k"))
print(arar.endswith("r"))
print(arar.endswith("to", 4, 10))