#!/usr/local/bin/python3
# variables-lists.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # tuple, an immutable object
    x = (1, 2, 3)
    print(type(x), x)
    for i in x:
        print(i)

    # list, mutable
    x = [1, 2, 3]
    print(type(x), x)
    x.append(5)
    print(x)
    x.insert(0, 7)
    print(x)
    for i in x:
        print(i)

    # string, an immutable object
    x = 'facetious'
    # one character, 'c'
    print(type(x), x[2])
    # slice, index 2 up to but not including 4, 'ce'
    print(type(x), x[2:4])
    for i in x:
        print(i)

if __name__ == "__main__": main()
