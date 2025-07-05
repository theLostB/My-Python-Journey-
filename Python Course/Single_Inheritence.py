class Animal:
    def __init__(self, name):
        self.name = name
       
    def make_sound(self):
        print("Sound by the animal")
        
class Cat(Animal):
        def __init__(self, name):
            Animal.__init__(self, name)
            
        def make_sound(self):
            print("Meow Meow")
        #Here we have a child class which have one parent that's why it is single inheritance 
cat = Animal("Cat")
cat.make_sound()

cat_0 = Cat("Cat")
cat_0.make_sound()