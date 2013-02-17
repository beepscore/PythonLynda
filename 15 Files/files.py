#!/usr/bin/env python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # Open file
    # http://docs.python.org/3/library/functions.html#open
    # Explicitly specify read mode. Alternatively, if omit, default # is 'r'
    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w')

    # read file line by line
    for line in infile:
        # print to screen
        print(line, end = '')
        # print to outfile
        print(line, file = outfile, end = '')

    print('Done writing new.txt.')


    # read big file in buffered I/O chunks, not line by line
    buffersize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('bigfileout.txt', 'w')

    buffer = infile.read(buffersize)
    while len(buffer):
        print('.', end = '')
        outfile.write(buffer)
        buffer = infile.read(buffersize)

    print()
    print('Done writing bigfileout.txt.')

if __name__ == "__main__": main()
