#!/usr/bin/env python3

# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')

    # dictionary, some other languages call it an associative array

    my_dict = {'one' : 1, 'two' : 2, 'three' : 3}
    print(my_dict)

    another_dict = dict(one = 1, two = 2, three = 3)
    print(another_dict)

    # http://stackoverflow.com/questions/5008828/convert-a-python-type-object-to-a-string
    print(type(another_dict))
    print(another_dict.__class__.__name__)

    danny = dict(four = 4, five = 5, six = 6, **my_dict)
    print(danny)


    print('four' in danny)
    print(4 in danny)

    for key in danny:
        print(key)

    for key, value in danny.items():
        print(key, value)

    # referencing a key that doesn't exist would throw KeyError: 'thousand'
    # danny['thousand']
    print(danny.get('thousand'))
    # specify default value if not found
    print(danny.get('thousand', 'not found'))
    print(danny.get('two'))

    del danny['four']
    print(danny.pop('five'))

if __name__ == "__main__": main()
