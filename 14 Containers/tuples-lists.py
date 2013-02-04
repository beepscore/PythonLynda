#!/usr/bin/env python3

# env is more portable than this path
##!/usr/local/bin/python3

# tuples-lists.py by Steve Baker
# Based on Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the tuples-lists.py file.')

    # tuples, immutable
    # can create a tuple without ()
    firstTuple = 18, 2, 4
    print('firstTuple', firstTuple) 
    secondTuple = (6, 8, 3, 5)
    print('secondTuple', secondTuple) 

    print('Surrounding a number with () doesn\'t make it a tuple.')
    print('type((12)) is', type((12)) )
    print('To declare a tuple, use () and at least one comma.')
    print('type(12,) is', type((12,)) )


    print('secondTuple[0]', secondTuple[0]) 
    print('secondTuple[-1]', secondTuple[-1]) 
    print('len(secondTuple)', len(secondTuple)) 
    print('min(secondTuple)', min(secondTuple)) 
    print('max(secondTuple)', max(secondTuple)) 

    # immutable, gives TypeError: 'tuple' object does not support item assignment
    # secondTuple[2] = 13

    secondTuple = tuple(range(25))
    print('secondTuple', secondTuple)
    print('20 in secondTuple', 20 in secondTuple)
    print('40 in secondTuple', 40 in secondTuple)

    print('number of occurences of 20 in secondTuple = secondTuple.count(20) :', secondTuple.count(20))
    print('number of occurences of 40 in secondTuple = secondTuple.count(40) :', secondTuple.count(40))

    print('index of 20 in secondTuple = secondTuple.index(20) :', secondTuple.index(20))
    # gives ValueError: tuple.index(x): x not in tuple
    # print('index of 40 in secondTuple = secondTuple.index(40) :', secondTuple.index(40))

    for element in secondTuple:
      print(2*element)

    # lists, mutable
    print('type[12] is', type([12]) )

    firstList = [6, 8, 3, 5]
    print('firstList', firstList) 

    firstList[2] = 42
    print('firstList', firstList) 

    firstList.append(17)
    print('firstList', firstList) 
    # to add multiple items, use extend
    firstList.extend(range(20))
    print('firstList', firstList) 
    firstList.insert(2, 99)
    print('firstList', firstList) 
    # insert inserts object before index.
    # insert at len is the same as append
    firstList.insert(len(firstList), 777)
    print('firstList', firstList) 
    # remove first element with value 8
    firstList.remove(8)
    print('firstList', firstList) 
    del firstList[2]
    #print('del firstList[2]', firstList) 
    #pop with no argument pops and returns the last element
    print('firstList.pop()', firstList.pop())
    print('firstList', firstList) 
    print('firstList.pop(5)', firstList.pop(5))
    print('firstList', firstList) 

if __name__ == "__main__": main()
