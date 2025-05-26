#!/usr/bin/python3
'''
A module include a function that checks it an object is an instance of
a calss that inherited (directly or indirectly) from the specified class.
'''


def inherits_from(obj, a_class):
    '''
    The method that checks the inheritance
    Args:
        obj: The object checked
        a_class: The class to check against
    Returns:
            True is is subclass, False otherwise
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
