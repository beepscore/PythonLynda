#!/usr/local/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# References
# Python documentation, standard library
# http://docs.python.org/3/library/stdtypes.html
# http://docs.python.org/3/library/stdtypes.html#string-methods

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

    # format()

    # Python 2.x used C style format specifiers. To print an object, you need to know and specify its type.
    # Python 3.0 added string.format(). It uses repr to print any type of object, don't need to specify type.
    # Python 3.0 required positional or name indicator number inside {}.
    a, b = 5, 2
    # Python 3.1 infers from order. You can change order using positional indicator or name.
    print('a:{} b:{}'.format(a, b))

    # format with positional indicator
    print('a:{0} b:{1}'.format(a, b))
    print('a:{1} b:{0}'.format(b, a))

    # format with name indicator
    print('a:{alpha} b:{beta}'.format(alpha = a, beta = b))

    # format with dictionary
    d = dict(alpha = a, beta = b)
    print('a:{alpha} b:{beta}'.format(**d))
    print()

    # split at separator and remove separator. Default separator is whitespace.
    s = 'this is a string of words'
    print(s.split())
    print(s.split('i'))
    # could iterate over this list of words
    words = s.split()
    print(words)

    # join words with a colon
    newString = ':'.join(words)
    print(newString)
    csvString = ', '.join(words)
    print(csvString)


    myString = 'this is my fluffy string'
    print(myString.center(40, '*'))

if __name__ == "__main__": main()
