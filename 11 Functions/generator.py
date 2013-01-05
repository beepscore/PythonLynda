#!/usr/local/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the generator.py file.")
    for i in inclusive_range_start_stop_step(0, 25, 1):
        print(i, end = ' ')
    print()

    # Call with one argument stop
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

    # Call with two arguments start, stop
    for i in inclusive_range(3, 12):
        print(i, end = ' ')
    print()

    # Call with three arguments start, stop, step
    for i in inclusive_range(3, 12, 2):
        print(i, end = ' ')
    print()

    # Call with four arguments
    #for i in inclusive_range(3, 12, 2, 5):
        #print(i, end = ' ')
    #print()

# Python standard range is non-inclusive of stop.
# Define an inclusive range
# inclusive_range_start_stop_step() uses "yield". It's a generator function.
# It returns an iterator object that can be used in a for loop.
# Require all three arguments
def inclusive_range_start_stop_step(start, stop, step):
    i = start
    while i <= stop:
        # yield returns a value, then resumes loop
        yield i
        i += step

# Allow call with one argument stop, 
# two arguments start, stop, 
# or three arguments
def inclusive_range(*args):

    numberOfArguments = len(args)

    if numberOfArguments < 1:
        raise TypeError('inclusive_range caller must supply at least one argument stop')
    elif numberOfArguments ==  1:
        start = 0
        stop = args[0]
        step = 1
        return inclusive_range_start_stop_step(start, stop, step)
    elif numberOfArguments ==  2:
        (start, stop) = args
        step = 1
        return inclusive_range_start_stop_step(start, stop, step)
    elif numberOfArguments ==  3:
        (start, stop, step) = args
        return inclusive_range_start_stop_step(start, stop, step)
    else:
        message = 'inclusive_range expected at most three arguments, got {}'.format(numberOfArguments)
        raise TypeError(message)

    
if __name__ == "__main__": main()

