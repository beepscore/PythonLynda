#!/usr/local/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():

    try:
        # for this exercise, purposely misspell file name in order to create an error.
        # lines = readfile('lines.txt')
        # lines = readfile('xlines.txt')
        lines = readfile('xlines.doc')

    except FileNotFoundError as fileError:
        print('Couln\'t open the file.', fileError)

    # catch the exception defined in readfile
    except ValueError as valueError:
        print('Bad filename.', valueError)

    else:
        # strip removes any trailing newlines from end of string, then print adds one.
        for line in lines: print(line.strip())

def readfile(filename):
    if not filename.endswith('.txt'):
        # raise our own exception, name it ValueError
        raise ValueError('Filename must end with .txt')
    else:
        fh = open(filename)
        return fh.readlines()

if __name__ == "__main__": main()
