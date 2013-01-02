#!/usr/local/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():

    # compile regular expression pattern instead of interpretively evaluating each iteration.
    # compiling allows use of re.IGNORECASE and method pattern.sub()
    # ignore case in order to match Nevermore or nevermore
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)

    fh = open('raven.txt')
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')
    print('-------------------------------')
    print()

    # after running loop above, must re-assign fh. Why?
    # Does python automatically close file when iterator reaches the end?
    fh = open('raven.txt')
    for line in fh:
        match = re.search(pattern, line)
        if match:
            print(match.group())
    print('-------------------------------')
    print()

    print('substitute, i.e. search and replace')
    fh = open('raven.txt')
    for line in fh:
        # print every line
        # pattern.sub uses regular expression module to perform substitution.
        # regular expression engine substitution is faster than string object's substitution.
        # print(re.sub(pattern, 'Al Gore', line), end='')        
        print(pattern.sub('Al Gore', line), end='')
    print('-------------------------------')
    print()

    print('first search, then replace')
    fh = open('raven.txt')
    for line in fh:
        # search
        match = re.search(pattern, line)
        if match:
            # replace
            print(line.replace(match.group(), 'Al Gore'), end='')
    print('-------------------------------')
    print()

if __name__ == "__main__": main()
