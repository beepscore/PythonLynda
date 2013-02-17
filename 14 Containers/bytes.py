#!/usr/bin/env python3

# bytes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the bytes.py file.')
    print()
    fin = open('utf8.txt', 'r', encoding = 'utf_8')
    fout = open('utf8.html', 'w')

    # bytearray is a mutable list of bytes
    outbytes = bytearray()
    for line in fin:
        for c in line:
            # ord() returns integer equivalent of character
            if ord(c) > 127:
                # character is non-ASCII. Replace character with xml unicode entity
                escaped_bytes = bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
                outbytes += escaped_bytes
            else:
                # character is ASCII. Just append it to outbytes.
                outbytes.append(ord(c))

    # convert bytes to string
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr)
    print(outstr, file = fout)
    print('Done')


if __name__ == "__main__": main()
