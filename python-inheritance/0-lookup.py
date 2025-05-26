#!/usr/bin/python3
'''
module to returns the list of available attributes and methods of an object
'''

def lookup(obj):
    '''
    returns the list of available attributes and methods object
    Args:
        obj: object to look up
    '''
    return dir(obj)
