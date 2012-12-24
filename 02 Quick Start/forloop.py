#!/usr/local/bin/python3

# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines():
    # In Python 3, print() is a function and requires parentheses.
    # Set print end to empty string '' instead of default newline '\n'
    # After setting end, Janus Macvim Syntastic plugin warns syntax error but script runs ok.
    print(line, end='')
