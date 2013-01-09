#!/usr/local/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print()
    
    # find returns the index of the first letter. Finds 'is' in this, returns 2.
    print(s.find('is'))

    print(s.replace('this', 'that'))
    # strips from beginning and end of string. Default is to strip whitespace, including newline.
    print(s.strip())
    # rstrip() removes from right end only.
    print('blah\n')
    print('blah\n'.rstrip('\n'))

    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())

    # Python strings are immutable. stringWithNumbers is a different object than stringWithBraces
    stringWithBraces = 'this is {}, that is {}'
    stringWithNumbers = stringWithBraces.format(5, 42)
    print(stringWithBraces, 'id(stringWithBraces):', id(stringWithBraces))
    print(stringWithNumbers, 'id(stringWithNumbers):', id(stringWithNumbers))

if __name__ == "__main__": main()
