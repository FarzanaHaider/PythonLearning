# Prevents a user function creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("The car is going")

    def stop(self):
        print("The car is stopped")

class Motorbike(Vehicle):

    def go(self):
        print("The motorbike is going")

    def stop(self):
        print("The motorbike is stopped")

# vehicle = Vehicle()
car = Car()
motorbike = Motorbike()

car.go()
motorbike.stop()
