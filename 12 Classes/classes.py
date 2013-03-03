#!/usr/bin/env python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Animal:
    def clothes(self):
        print('I have nice clothes')

    def talk(self):
        print('I have something to say!')

    def walk(self):
        print('Hey! I\'m walkin\' here!')


class Dog(Animal):
    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def quack(self):
        print('The dog cannot quack')

    def walk(self):
        print('Walks like a dog.')


class Duck(Animal):

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

    def bark(self):
        print('The duck cannot bark')

    def fur(self):
        print('The duck has feathers')

    def quack(self):
        print('Quaaack!', self._value)

    # override super's definition, but call super also
    def walk(self):
        super().walk()
        print('Walks like a duck.', self._value)


class Wombat(Animal):
    # use keyword arguments dictionary, this technique scales well as number of arguments increases
    def __init__(self, **kwargs):
        self._variables = kwargs

    # Accessors enable an object to manage it's own concerns.
    def get_variable(self, key):
        # if _variables doesn't have the key, this statement would cause a KeyError
        # return self._variables[key]
        # if key isn't found, add key/value pair with default value None.
        return self._variables.get(key, None)

    def set_variable(self, key, value):
        if key == 'color':
            # use custom setter for color
            self.set_color(value)
        else:
            # use 'generic' setter
            self._variables[key] = value

    # This setter checks input validity.
    # Some setters set the instance variable and then update a database.
    def set_color(self, color):
        if type(color) is not str:
                print('color must be a string')
        else:
            self._variables['color'] = color


def in_the_forest(anAnimal):
    anAnimal.bark()
    anAnimal.fur()


def in_the_pond(duck):
    duck.quack()
    duck.walk()


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
    print('willy color:', willy.get_variable('color'))
    wanda = Wombat(color = 'blue')
    print('wanda color:', wanda.get_variable('color'))
    wanda.set_variable('color', 'indigo')
    print('wanda color:', wanda.get_variable('color'))

    warren = Wombat(feet = 4)
    print('warren feet:', warren.get_variable('feet'))
    print()

    # Experiment with inheritance and polymorphism
    fido = Dog()

    # Polymorphism - different classes can implement the same method differently
    for aCritter in (donald, fido):
        aCritter.bark()
        aCritter.clothes()
        aCritter.fur()
        aCritter.quack()
        aCritter.talk()
        aCritter.walk()
        print()

    # python is loosely typed (duck typed).
    # any object that implements the method will work.
    in_the_forest(donald)
    print()
    in_the_pond(fido)

if __name__ == "__main__": main()
