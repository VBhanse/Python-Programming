class Animal: #Parent class(superclass)
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now...")

class Dog(Animal): #This is inheritance is done in Python
    def speak(self):
        super().speak()#We are using the speal function of the parent class
        print("Woof")

a = Animal("Dog")
a.speak()
d = Dog("Bruno")
d.speak()
# print(d.location)
