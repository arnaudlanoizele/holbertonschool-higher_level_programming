#!/usr/bin/python3
'''
This module contains a single class suqare
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
    This class implement a square based on rectangle
    Args:
        size: The size of the square
    '''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        return self.__size * self.__size
