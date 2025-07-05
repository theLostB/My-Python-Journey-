try:
    l = [1, 2, 4, 8, 16]
    i = int(input("Enter any index:"))
    print(l[i])
except:
    print("Some error occurred")
finally:
    print("I am always execute")