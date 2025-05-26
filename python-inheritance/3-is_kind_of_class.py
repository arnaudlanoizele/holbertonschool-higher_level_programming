#!/usr/bin/python3
'''
This module provides a method that checks if an objet is an instance
of a class or a subclass of that inherited from
'''


def is_kind_of_class(obj, a_class):
    '''
    This method checks if the objet is an instance
    Args:
        obj: The objet to check
        a_class: The class to check against
    Returns:
            True if obj is an instance of a_class, False if not
    '''
    return isinstance(obj, a_class)
