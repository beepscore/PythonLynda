#!/usr/local/bin/python3

# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# Using main() allows calling any function as long as it appears somewhere in the script.
# If not using main(), function must appear before calling it.
def main():
    print("This is the syntax.py file.")
    egg()

def egg():
    print("egg")

# If script is run as the main module (e.g. from the command line), __name__ will equal "__main__" and the script will call main()
# If script is included in a different module, it won't automatically call main().
if __name__ == "__main__": main()
