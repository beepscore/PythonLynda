#!/usr/local/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # read the lines from the file
    fh = open('lines.txt')

    # readlines() method is an iterator
    for line in fh.readlines():
        # In Python 3, print() is a function and requires parentheses.
        # Set print end to empty string '' instead of default newline '\n'
        # After setting end, Janus Macvim Syntastic plugin warns syntax error but script runs ok.
        print(line, end='')

    # In python all container objects (tuples, strings) are iterators
    for item in [1, 2, 3, 4]:
        # print() inserts space between item and empty string. The line will end with a space.
        print(item, '', end='')
    print()

    for letter in 'the world of sleeping dogs':
        # print() inserts space between item and empty string. The line will end with a space.
        print(letter, '', end='')
    print()

if __name__ == "__main__": main()
