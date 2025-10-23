class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def sound(self):
        return "Мяу!"

class Parrot(Animal):
    def sound(self):
        return "Чирик!"

animals = [Dog(), Cat(), Parrot()]

for animal in animals:
    print(animal.sound())
