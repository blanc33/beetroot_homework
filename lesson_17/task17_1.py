class Animal:
    @staticmethod
    def talk():
        print("Some awkward sound.")

class Dog(Animal):
    @staticmethod
    def talk():
        print("Woof!")

class Cat(Animal):
    @staticmethod
    def talk():
        print("Meow!")

pig = Animal()
cat = Cat()
dog = Dog()
animals = [pig, cat, dog]
for animal in animals:
    animal.talk()