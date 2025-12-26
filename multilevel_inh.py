class Animal:
    def eat(self):
        print("Animal can eat")
class Mammal(Animal):  
    def walk(self):
        print("Mammal can walk")
class Dog(Mammal): 
    def bark(self):
        print("Dog can bark")
my_dog = Dog()
my_dog.eat()    
my_dog.walk()   
my_dog.bark()  
