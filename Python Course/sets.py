s = {2, 4, 2, 6, "rishaank", "set", "python"}
print(type(s))
print(s)#Sets does not repeat value if you give two times same value  python does not take it , it return only one value...            And sets dsoes not maintain order
ar = {}
print(type(ar))
ar = set()
print(type(ar))
for value in s:
    print(value)
    
s1 = {1, 3, 5, 82, 29, 2,}
s2 = {3, 39, 92, 0, 4, 1 ,7}
print(s1.union(s2))#.union is use for merging the sets...
s1.update(s2)#Update method is use to update the set... here update means add all those value of s2 that is not in s1, add it to s1...
print(s1)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
cities3 = cities.intersection(cities2)#This method is use to see which value are double in sets...
print(cities3)
cities.intersection_update(cities2)
print(cities)
cities3 = cities.symmetric_difference(cities2)#This method is used to print those value which is not common in sets..
print(cities3)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seol", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)#This method is used to print those values which present in original set but not in both sets..
print(cities3)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seol", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)
print(cities3)
#isdisjoint method is use to check that those values which is present in original set are present in both set or not if present in both sets it give false and if not present it gives true...
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seol", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seol", "Kabul", "Madrid"}
print(cities.issuperset(cities2))
# issuperset method is use to check that those values which is present in particular set is present in original set or not if present it gives true else false 
cities3 = {"Seol", "Kabul", "Madrid"}
print(cities.issuperset(cities))
print(cities3.issubset(cities))