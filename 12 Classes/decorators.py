#!/usr/local/bin/python3
# decorators.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# Decorators are functions that return other functions
# Python decorators are most commonly used to make accessors.

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    donald = Duck(color = 'blue')
    print(donald.get_property('color'))
    print()

    donald.color = 'yellowish'
    print(donald.color)
    print()

    del(donald.color)
    print(donald.color)
    print()

if __name__ == "__main__": main()
