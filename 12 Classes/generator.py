#!/usr/local/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# In Chapter 11 defined inclusive_range as a function.
# Here in Chapter 12 define inclusive_range as a class.

# Python standard range is non-inclusive of stop.
# Define an inclusive range
class inclusive_range:

    def __init__(self, *args):
        # Allow call with one argument stop, 
        # two arguments start, stop, 
        # or three arguments start, stop, step.
        numberOfArguments = len(args)

        if numberOfArguments < 1:
            raise TypeError('inclusive_range caller must supply at least one argument stop')
        elif numberOfArguments ==  1:
            self._start = 0
            self._stop = args[0]
            self._step = 1
        elif numberOfArguments ==  2:
            (self._start, self._stop) = args
            self._step = 1
        elif numberOfArguments ==  3:
            (self._start, self._stop, self._step) = args
        else:
            message = 'inclusive_range expected at most three arguments, got {}'.format(numberOfArguments)
            raise TypeError(message)


    # implementing __iter__ makes object iterable when used in an iterative context such as a loop.
    # returns an generator object.
    def __iter__(self):
        i = self._start
        while i <= self._stop:
            # yield returns a value, then resumes loop.
            yield i
            i += self._step


def main():

    # instantiate an inclusive range
    # o = inclusive_range(25)
    # o = inclusive_range(5, 25, 7)
    # o = inclusive_range()
    # o = inclusive_range(5, 25, 7, 38)
    o = inclusive_range(5, 25, 2)

    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
