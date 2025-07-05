class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def showDetails(self):
        print(f'Name: {self.name}')
        print(f'Species: {self.species}')
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    def showDetails(self):
        Animal.showDetails(self)
        print(f'Breed: {self.breed}')
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed='Golden Retriever')
        self.color = color
        
    def showDetails(self):
        Dog.showDetails(self)
        print(f'Colour: {self.color}')
        
o = GoldenRetriever("Tommy", "Black")
o.showDetails()