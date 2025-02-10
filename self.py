# Vad gör följande kod? Fixa eventuella fel
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(shelf):
        super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        super().make_noise()
        print("Pip!")

class Fish(Animal):
    def make_noise(self):
        super().make_noise()
        print("Blubb!")

def sound_off(animal): 
    for a in animal:
        a.make_noise() 


c = Cat()
d = Dog()
h = Rooster()
f = Fish()
sound_off([c, d, h, f])
