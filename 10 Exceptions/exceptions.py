#!/usr/local/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():

    try:
        # for this exercise, purposely misspell file name in order to create an error.
        # fh = open('lines.txt')
        fh = open('xlines.txt')

    # catch only FileNotFoundError
    except FileNotFoundError as fileError:
        print('Couln\'t open the file.', fileError)
    else:
        # strip removes any trailing newlines from end of string, then print adds one.
        for line in fh: print(line.strip())

if __name__ == "__main__": main()
