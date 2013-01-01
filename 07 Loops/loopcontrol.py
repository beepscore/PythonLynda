#!/usr/local/bin/python3
# loopcontrol.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Portions copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'

    for c in s:
        # continue exits this iteration
        if 's' == c: continue
        print(c, end='')
    print()

    for c in s:
        # break exits the entire loop
        if 's' == c: break
        print(c, end='')
    print()

    for c in s:
        print(c, end='')
    else:
        print()
        print('Loop finished')

if __name__ == "__main__": main()
