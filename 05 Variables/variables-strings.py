#!/usr/local/bin/python3
# variables-strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'This is a string!'
    print(s)
    anEscapedString = 'This is a\nstring!'
    print(anEscapedString)

    # raw strings are sometimes used for regular expressions
    aRawString = r'This is a\nstring!'
    print(aRawString)

    aNumber = 42
    # Python 2 style (deprecated)
    formattedString = 'This is a string with %s' % aNumber
    print(formattedString)
    # In Python 3 call string object's method format()
    formattedString = 'This is a string with {}'.format(aNumber)
    print(formattedString)

    # triple quote for multiple lines. Backslash escapes the leading newline.
    multiLineString = '''\
one
two
three'''
    print(multiLineString)        
            

if __name__ == "__main__": main()
