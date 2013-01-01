#!/usr/local/bin/python3
# for-enumerate.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Portions copyright 2010 The BearHeart Group, LLC

def main():
    # read the lines from the file
    fh = open('lines.txt')

    # readlines() method is an iterator
    for index, line in enumerate(fh.readlines()):
        # In Python 3, print() is a function and requires parentheses.
        # Set print end to empty string '' instead of default newline '\n'
        # After setting end, Janus Macvim Syntastic plugin warns syntax error but script runs ok.
        print(index, line, end='')

    # In python all container objects (tuples, lists, strings) are iterators
    aList = [1, 2, 3, 4]
    for index, item in enumerate(aList):
        print(item, end='')
        # if on last item don't append space
        # In python len() is a function, not an object method
        # References:
        # http://www.effbot.org/pyfaq/why-does-python-use-methods-for-some-functionality-e-g-list-index-but-functions-for-other-e-g-len-list.htm
        # http://lucumr.pocoo.org/2011/7/9/python-and-pola/
        if index < (len(aList) - 1):
            print(' ', end='')
    print()

    dogTitle = 'the world of sleeping dogs'
    for index, letter in enumerate(dogTitle):
        print(letter, end='')
        # if on last item don't append space
        if index < (len(dogTitle) - 1):
            print(' ', end='')
    print()

    for index, letter in enumerate(dogTitle):
        searchLetter = 'e'
        if searchLetter == letter:
            print('found {} at index {}'.format(searchLetter, index))
    print()

if __name__ == "__main__": main()
