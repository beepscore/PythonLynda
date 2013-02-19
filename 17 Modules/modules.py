#!/usr/bin/env python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# <http://docs.python.org/3/library/index.html>
# <http://docs.python.org/3/library/sys.html>

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print('sys.platform {}'.format(sys.platform))

    # can import within a function
    import os
    print('os.name {}'.format(os.name))

    print("os.getenv('PATH') {}".format(os.getenv('PATH')))
    print("os.getcwd() {}".format(os.getcwd()))

    # urandom(n) returns n random bytes
    print("os.urandom(25) {}".format(os.urandom(25)))

    import urllib.request
    page = urllib.request.urlopen('http://bw.org/')
    for line in page:
        # print(str(line, encoding = 'utf_8'), end = '')
        pass

    import random
    print(random.randint(1, 1000))
    x = list(range(25))
    print('x {}'.format(x))
    random.shuffle(x)
    print('shuffle(x) {}'.format(x))

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.minute, now.second, now.microsecond)


if __name__ == "__main__": main()
