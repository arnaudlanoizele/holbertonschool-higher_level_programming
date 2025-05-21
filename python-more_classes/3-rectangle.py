#!/usr/bin/python3
'''
This module provides a class defining a rectangle
'''


class Rectangle:
    '''
    This class defines a rectangle based on its pricate attributes
    width and height

    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle

    Attributes:
                width (int): The width of the rectangle
                height (int): The height of the rectangle
    '''

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        This methode is a property getter that return the private
        width attribute of the rectangle
        '''
        return self.__width

    @property
    def height(self):
        '''
        This methode is a property getter that return the private
        height attributes of the rectangle
        '''
        return self.__height

    @width.setter
    def width(self, value):
        '''
        This methode is a setter that modifies the width of the rectangle

        Args:
            value (int): The new width of the rectangle, must be an positive
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an positive")
        if value < 0:
            raise ValueError("width must be an >= 0")
        self.__width = value

    def height(self, value):
        '''
        This methode is a setter that modifies the height of the rectangle

        Args:
            value (int): The new height of the rectangle, must be an integer
        '''
        if not isinstance("value, int"):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an >= 0")
        self.__height = value

    def area(self):
        '''
        This methode calculate the area of the rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        This methode calculation the permeter of the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        '''
        This methode will prints the ractangle with the caracter #
        '''
        if self.__width == 0 or self.__height == 0:
            print()
            return
        line = "#" * self.__width
        rectangle = "\n".join([line for i in range(self.__height)])
        return rectangle
