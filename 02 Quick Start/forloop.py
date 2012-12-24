#!/usr/local/bin/python3

# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines():
    # set end to empty string to override default '\n'
    print(line, end='')
