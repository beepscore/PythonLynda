#!/usr/local/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():

    #instantiate a Duck
    donald = Duck()
    print(donald)

    # method call implicitly supplies argument 'self', a reference to the caller
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
