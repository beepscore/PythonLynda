#!/usr/local/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    emptyFunc()
    testFuncOne(42, 16)
    testFuncTwo(38)
    testFuncThree(1, 2, 3, 42, 43, 45, 46)

    # caller names the arguments, not the function def
    funcWithKeywordArgs(one = 1, two = 2, four = 42)


def emptyFunc():
    # pass acts like a nop, can be used to stub a function or method body and avoid syntax error.
    pass

# assigning default parameter value in function definition means caller can omit it.
def testFuncOne(number, another = 43, oneMore = 75):
    print('testFuncOne:', number, another, oneMore)

# None is a system singleton object
def testFuncTwo(number, another = None, oneMore = 75):
    print('testFuncTwo:', number, another, oneMore)
    if another is None : another = 112
    print('testFuncTwo:', number, another, oneMore)

# args is a tuple of arbitrary length
def testFuncThree(this, that, other, *args):

    # syntastic warns syntax error but it runs.
    # output: testFuncThree: 1 2 3 42 43 45 46
    print('testFuncThree:', this, that, other, *args)

    # this prints args as a tuple
    # output: testFuncThree: 1 2 3 (42, 43, 45, 46)
    print('testFuncThree:', this, that, other, args)

    # tuple will print in order
    for n in args: print(n, end = ' ')
    print()


# kwargs is a dictionary, caller specifies keys
# ==> Function doesn't know names before it is called.
def funcWithKeywordArgs(**kwargs):
    print('funcWithKeywordArgs:', kwargs['one'], kwargs['two'], kwargs['four'])

    # kwargs dictionary items may appear in any order
    for key in kwargs:
        print(key, kwargs[key])

if __name__ == "__main__": main()
