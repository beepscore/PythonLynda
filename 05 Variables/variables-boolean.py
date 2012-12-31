#!/usr/local/bin/python3
# variables-boolean.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    a, b = False, True
    print('True type:{0} id:{1} {2}'.format(type(True), id(True), True))
    print('a type:{0} id:{1} {2}'.format(type(a), id(a), a))
    print('b type:{0} id:{1} {2}'.format(type(b), id(b), b))
    
    # check if objects have equal values
    print('b == a', (b == a))
    
    # check if b is the same object as a
    print('b is True', (b is True))
    print('b is a', (b is a))
    
if __name__ == "__main__": main()
