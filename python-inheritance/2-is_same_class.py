#!/usr/bin/python3
'''
This module provides a function to check if an object
is exactly an instance of a specified class
'''


def is_same_class(obj, a_class):
    '''
    Thise methode chacks if an object is an instance of a class
    Args:
        obj: The objet to check
        a_class: The class to check against
    Returns:
            True if obj is an instance of a_class, False if not
    '''
    return type(obj) is a_class
