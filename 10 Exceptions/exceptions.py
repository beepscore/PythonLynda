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

    # catch exception raised in readfile
    except ValueError as valueError:
        print('Bad filename.', valueError)

    else:
        # strip removes any trailing newlines from end of string, then print adds one.
        for line in lines: print(line.strip())

def readfile(filename):
    if not filename.endswith('.txt'):
        # Python best practice: use built-in exceptions such as ValueError.
        # You could define your own, but generally not necessary to use non-standard exceptions.
        # http://docs.python.org/3/library/exceptions.html
        raise ValueError('Filename must end with .txt')

    else:
        fh = open(filename)
        return fh.readlines()

if __name__ == "__main__": main()
