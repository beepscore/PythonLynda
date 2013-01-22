#!/usr/bin/env python3

# env is more portable than this path
##!/usr/local/bin/python3

# tuples-lists.py by Steve Baker
# Based on Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the tuples-lists.py file.')

    # tuples, immutable
    firstTuple = 18, 2, 4
    print('firstTuple', firstTuple) 
    secondTuple = (6, 8, 3, 5)
    print('secondTuple', secondTuple) 

    print('secondTuple[0]', secondTuple[0]) 
    print('secondTuple[-1]', secondTuple[-1]) 
    print('len(secondTuple)', len(secondTuple)) 
    print('min(secondTuple)', min(secondTuple)) 
    print('max(secondTuple)', max(secondTuple)) 

    print('Surrounding a number with () doesn\'t make it a tuple.')
    print('type((12)) is', type((12)) )
    print('To declare a tuple, use () and at least one comma.')
    print('type(12,) is', type((12,)) )

    # immutable, gives TypeError: 'tuple' object does not support item assignment
    secondTuple[2] = 13


    # lists, mutable
    print('type[12] is', type([12]) )


if __name__ == "__main__": main()
