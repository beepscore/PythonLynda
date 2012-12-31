#!/usr/local/bin/python3
# variables-id.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    a = 63
    b = 63
    print('a type:{0} id:{1} {2}'.format(type(a), id(a), a))
    print('b type:{0} id:{1} {2}'.format(type(b), id(b), b))
    # check if objects have equal values
    print('b == a', (b == a))
    # check if b is the same object as a
    print('b is a', (b is a))
    
    # dictionary, mutable
    dictOne = dict(x = 42)
    dictTwo = dict(x = 42)
    print('dictOne type:{0} id:{1} {2}'.format(type(dictOne), id(dictOne), dictOne))
    print('dictTwo type:{0} id:{1} {2}'.format(type(dictTwo), id(dictTwo), dictTwo))

    # check if objects have equal values
    print('dictTwo == dictOne', (dictTwo == dictOne))

    # check if dictTwo is the same object as dictOne
    print('dictTwo is dictOne', (dictTwo is dictOne))
            
if __name__ == "__main__": main()
