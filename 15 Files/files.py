#!/usr/bin/env python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # Open file
    # http://docs.python.org/3/library/functions.html#open
    # Explicitly specify read mode. Alternatively, if omit, default # is 'r'
    f = open('lines.txt', 'r')

    for line in f:
        print(line, end = '')


if __name__ == "__main__": main()
