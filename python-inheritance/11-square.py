#!/usr/bin/python3
'''
Thise module contains a single class
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
    This class implement a suqare based on rectangle
    Args:
        size: The size of the square
    '''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().init__(size, size)
        self.size = size

    def __str__(self):
        return super().__str__().replace("Rectangle", "Square")

    def area(self):
        return self.__size * self.__size
