#!/usr/local/bin/python3
# variables-dictionary.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # dictionary, mutable
    # this syntax is less common
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    print(type(d), d)
    for key in d:
        print(key, d[key])

    print()
    print('sort keys in alphabetical order')
    for key in sorted(d.keys()):
        print(key, d[key])

    # dict constructor is more common
    g = dict(one = 1, two = 2, three = 3, four = 4, five = 'five')
    g['seven'] = 7
    print()
    for key in sorted(g.keys()):
        print(key, g[key])
            
if __name__ == "__main__": main()
