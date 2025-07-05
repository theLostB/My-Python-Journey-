dict = {
       "Rishaank": "Human being",
       "Spoon": "Object",
       567: "Harry",
       87: "Zakir",
       192: "Shubham",
       23: "Rishaank"
}
print(dict["Rishaank"])
print(dict[567])
print(dict[23])
print(dict.get(233))#this will exactly work like dict[] but we use .get when we not want to get error we want get none when the key is not in dictionary but at this time if we use dict[] it throw error

print(dict)