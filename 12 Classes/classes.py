#!/usr/local/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    def __init__(self, value):
        self._value = value
        print('constructor')


    def quack(self):
        print('Quaaack!', self._value)

    def walk(self):
        print('Walks like a duck.', self._value)

def main():

    #instantiate a Duck, calls the constructor __init__
    donald = Duck(47)
    print(donald)
    frank = Duck(151)
    print(frank)

    # method call implicitly supplies argument 'self', a reference to the caller
    donald.quack()
    donald.walk()
    frank.quack()
    frank.walk()

    print()

    # can access an object's instance variable directly, but best practice is to use a getter and setter.
    print(donald._value)
    donald._value = 'boo'
    print(donald._value)

if __name__ == "__main__": main()
