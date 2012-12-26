#!/usr/local/bin/python3
# variable-numbers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # in Python dividing two integers doesn't truncate
    # integer division is //
    intResult = 42//9

    floatResult = 42/9
    roundTwoResult = round(42/9, 2)
    roundResult = round(42/9)
    print(intResult, floatResult, roundTwoResult, roundResult)

    moduloResult = 42 % 9
    print(moduloResult)

    # float is a constructor, instantiates a float, param is int
    a = float(42)

if __name__ == "__main__": main()
