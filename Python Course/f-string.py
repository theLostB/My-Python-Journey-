letter = "Hey my name is {} and I am from {}"
name = "Rishaank"
country = "India"
print(letter.format(name, country))
letter = "Hey my name is {} and I am from {}"
print(letter.format(country, name))
letter = "Hey my name is {1} and I am from {0}"
print(letter.format(country, name))
#The above code is all about format 
print(f"Hey my name is {name} and I am from {country}")#This is f-string