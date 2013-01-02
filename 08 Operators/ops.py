#!/usr/local/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


def main():
    print("This is the ops.py file.")
    print()

    #########################################

    print('bitwise operators')

    b(5)

    x, y = 0x55, 0xaa
    b(x)
    b(y)

    # bitwise or
    b(x | y)
    # bitwise and
    b(x & y)
    # bitwise exclusive or
    b(x ^ y)
    b(x ^ 0x03)
    # shift bits left 4 places.
    # right 4 get filled with zeros.
    # This multiplies number by 2**4 = 16
    b(0xff << 4)
    b(x << 4)

    # shift bits right 4 places.
    # left 4 get filled with zeros.
    # This divides number by 2**3 = 8
    b(0xff >> 3)
    b(x >> 3)

    #ones complement, operates on implementation word size, > 8 bits 
    b(~x)

    print()

    #########################################

    print('Comparison operators')
    print(5 <= 3)
    c, d = 5, 6

    print(c == d)
    # assignment not allowed inside print
    # print(c = d)

    # is returns true if both variables are the same object. checks id() for equality
    print(c is d)
    print(c is not d)

    # tuples use () and are immutable,  lists use [] and are mutable.
    # list
    f = [3]
    g = f
    print(g is f)
    # change value 0
    f[0] = 4
    print('f:{}'.format(f))
    print('g:{}'.format(g))
    print(g is f)
    print()

    #########################################

    print('Boolean operators')
    print(True and False)
    print(True or False)

    j = 'zero'
    k = 'one'
    print('compare alphabetical order')
    print("'{}' > '{}' is '{}'".format(j, k, j > k))

    if (1>0) and (j>k):
        print('and statement True')
    else:
        print('and statement False')

    print()

    #########################################
    
    print('range(start, stop[, step]) is a type')
    print('range doesn\'t include element specified by stop')
    # http://docs.python.org/3/library/stdtypes.html#typesseq-range

    myList = []
    # shorthand fill list 0-19
    myList[:] = range(20)
    print(myList)
    print()

    print('Slice operator')
    print('Returns a slice object representing the set of indices specified by a range')
    # http://docs.python.org/3/library/functions.html#slice

    mySliceOne = myList[1:10]
    print('myList[1:10]', mySliceOne)

    mySliceTwo = myList[1:20:4]
    print('myList[1:20:4]', mySliceTwo)
    print()

    print('object returned from slice can be used as an iterator')
    for element in mySliceTwo: print(element)
    print()
def b(n):
    print('{:08b}'.format(n))

if __name__ == "__main__": main()
