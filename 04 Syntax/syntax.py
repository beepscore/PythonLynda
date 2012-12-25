#!/usr/local/bin/python3

# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# An interpreted language such as Python has no compiler checking.
# A statement won't be evaluated unless/until execution reaches it.
# By declaring function main() and waiting until the end of the file to call main(),
# the interpreter will have scanned all declarations in the file before it attempts to use them.
# This allows declaring functions in any order.
# Without this, a declaration would have to appear before it is used.
def main():
    print("This is the syntax.py file.")
    egg()

def egg():
    print("egg")

# Python scripts often end with this line.
# If script is run as the main module (e.g. from the command line), __name__ will equal "__main__" and when the interpreter reaches the bottom of the file it will call main()
# If script is included in a different module, it won't automatically call main().
if __name__ == "__main__": main()
