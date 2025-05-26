#!/usr/bin/python3
'''
This module defines a class MyList that inherits from list
'''


class MyList(list):
    '''
    MyList class that inherits from list and has a method
    to print the list in sorted order
    '''
    def print_sorted(self):
        '''
        Prints the list in order
        '''
        print(sorted(self))
