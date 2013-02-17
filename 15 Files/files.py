#!/usr/bin/env python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # Python distinguishes between text and binary files,
    # whether the current operating system does or not.

    # Read and write a text file
    # http://docs.python.org/3/library/functions.html#open
    # Explicitly specify read mode. Alternatively, if omit, default # is 'r'
    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w')

    # read file line using line oriented I/O
    for line in infile:
        # print to screen
        print(line, end = '')
        # print to outfile
        print(line, file = outfile, end = '')

    print('Done writing new.txt.')


    # As an example, read and write a large text file using buffered I/O.
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


    # Read and write a binary file
    # Use buffered I/O.
    buffersize = 50000
    # In Python, binary file must be opened in binary mode.
    infile = open('olives.jpg', 'rb')
    outfile = open('olivesout.jpg', 'wb')

    buffer = infile.read(buffersize)
    while len(buffer):
        print('.', end = '')
        outfile.write(buffer)
        buffer = infile.read(buffersize)

    print()
    print('Done writing olivesout.jpg.')


if __name__ == "__main__": main()
