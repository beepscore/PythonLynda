#!/usr/local/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # Python doesn't have a switch statement
    # You can do something similar using a dictionary
    choices = dict(
            one = 'first',
            two = 'second',
            three = 'third',
            four = 'fourth',
            five = 'fifth',
    )
    v = 'three'

    # If dictionary doesn't have an entry for the key, this will give KeyError
    print('choices[v]: {}'.format(choices[v]))

    # handle default
    v = 'bazillion'
    # if get doesn't find entry for the key, it will return specified default
    print('choices.get(v, "other"): {}'.format(choices.get(v, "other")))

if __name__ == "__main__": main()
