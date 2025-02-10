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

def sound_off(animal): # lade in for loopen här i stället
    for a in animal:
        a.make_noise() # de här blir som    c.make_noise osv


c = Cat()
d = Dog()
h = Rooster()
sound_off([c, d, h])
