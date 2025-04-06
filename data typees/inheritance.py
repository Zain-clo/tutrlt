
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species



   


class Dog(Animal):
    def __init__(self, name, breed):
       
        super().__init__(name, species='Dog')  
        self.breed = breed

   
    def description(self):
        print(self.name, "is a ",self.species)
        print (self.name, "is a breed of a " ,self.breed)

my_dog = Dog(name="Buddy", breed="Golden Retriever")


print(my_dog.description())  
