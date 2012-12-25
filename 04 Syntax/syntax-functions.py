#!/usr/local/bin/python3

# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the syntax-functions.py file.")
    some_func()
    some_func()
    some_func()

def some_func():
    for i in range(10):
        print(i, end = ' ')
    print()

if __name__ == "__main__": main()
