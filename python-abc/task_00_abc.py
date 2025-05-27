#!/usr/bin/env python3
from abc import ABC, abstractmethod
'''
This module includes an abstract class and subclasses
'''


class Animal(ABC):
    '''
    Abstract class Animal
    '''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''
    Dog that inherits from the Animal class
    '''
    def sound(self):
        return "Bark"


class Cat(Animal):
    '''
    Cat that inherits from the Animal
    '''
    def sound(self):
        return "Meow"
