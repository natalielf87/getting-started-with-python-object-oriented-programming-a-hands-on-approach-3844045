"""
Polymorphism Challenge
"""


# Base class
class Animal:
    def make_sound(self):
        print("Generic animal sound")

# Subclass Dog


class Dog(Animal):
    def make_sound(self):
        print("Wof-Wof")

# Subclass Cat


class Cat(Animal):
    def make_sound(self):
        print("Meo-Meo")


# Create instances
my_dog = Dog()
my_cat = Cat()

# Test methods
my_dog.make_sound()
my_cat.make_sound()
