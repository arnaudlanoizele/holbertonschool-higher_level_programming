#!/usr/bin/python3
'''
This module include a class with multiple inheritence
'''


class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives oin water")

class Bird:
    def fly(self):
        print("The bird is flyiong")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying is soaring!")

    def swim(self):
        print("The flying is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
