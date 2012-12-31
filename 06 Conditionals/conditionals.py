#!/usr/local/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a, b = 0, 1
    if a < b:
        print('this is true')
    else:
        print('this is false')

    v = 'seven'
    # one and only one of these will execute
    # similar to other languages' switch statement
    if 'one' == v:
        print('v is one')
    elif 'two' == v:
        print('v is two')
    elif 'three' == v:
        print('v is two')
    else:
        # default case
        print('v is some other thing')

if __name__ == "__main__": main()
