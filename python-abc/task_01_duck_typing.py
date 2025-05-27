#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi as hw
'''
Module that implements Shape, Circle and Rectangle for duck typing
'''


class Shape(ABC):
    '''
    Abstract class for Shape
    '''
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    '''
    Circle that inherits from Shape
    '''
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return hw * self.__radius ** 2

    def perimeter(self):
        return 2 * hw * self.__radius

class Rectangle(Shape):
    '''
    Rectangle that inherits from Shape
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    '''
    A function simulating duck typing
    '''
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
