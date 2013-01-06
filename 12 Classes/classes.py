#!/usr/local/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    def __init__(self, value, color = 'white'):
        print('constructor')
        self._value = value
        self._color = color

    # Accessors enable an object to manage it's own concerns.
    def get_color(self):
        return self._color

    # This setter checks input validity.
    # Some setters set the instance variable and then update a database.
    def set_color(self, color):
        if type(color) is not str:
                print('color must be a string')
        else:
            self._color = color

    def quack(self):
        print('Quaaack!', self._value)

    def walk(self):
        print('Walks like a duck.', self._value)


class Wombat:
    # use keyword arguments, this scales better as number of arguments increases
    def __init__(self, **kwargs):
        self._variables = kwargs

    # Accessors enable an object to manage it's own concerns.
    def get_color(self):
        # if _variables doesn't have a key color, this statement would cause a KeyError
        # return self._variables['color']
        # if color isn't found, add key/value pair with default value None.
        return self._variables.get('color', None)

    # This setter checks input validity.
    # Some setters set the instance variable and then update a database.
    def set_color(self, color):
        if type(color) is not str:
                print('color must be a string')
        else:
            self._variables['color'] = color

            
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

    # It's possible to access an object's instance variable directly.
    # However best practice is to use a getter and setter.
    donald._color = 'blue'
    print(donald._color)
    # Accessing ivar directly enables accidentally setting _color to an invalid value.
    donald._color = 12
    print(donald._color)
    print()

    donald.set_color('green')
    print(donald.get_color())
    # Duck set_color() won't set color to a number.
    donald.set_color(12)
    print(donald.get_color())
    print()

    willy = Wombat()
    print('willy', willy.get_color())
    wanda = Wombat(color = 'blue')
    print('wanda', wanda.get_color())

if __name__ == "__main__": main()
