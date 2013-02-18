#!/usr/bin/env python3

# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# Python comes with sqlite
# sqlite is simple to use. Doesn't require setting up a server
# mySQL requires setting up a server.
# http://docs.python.org/3.3/library/sqlite3.html
import sqlite3

def main():
    print('This is the databases.py file')

    # At first sqlite3.connect failed, and didn't create test.db
    # In terminal ran
    # $ brew uninstall python3
    # $ brew uninstall sqlite3
    # $ brew uninstall sqlite
    # $ brew install python3
    # This reinstalled dependency sqlite3, reinstalled Python.
    # This fixed the problem.
    # Reference:
    # http://bind10.isc.org/wiki/SystemNotesMacOSXMountainLion

    # Can view sqlite database binary file with Firefox plugin SQLiteManager

    db = sqlite3.connect('test.sqlite')

    # Row factory is very powerful.
    # Enables Python to get objects from sqlite
    # Row provides both index-based and case-insensitive name-based access to columns
    db.row_factory = sqlite3.Row

    # delete old table
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    # after changing data, must commit it.
    db.commit()
    # sort by t1 text field
    cursor = db.execute('select * from test order by t1')

    for row in cursor:
        # dictionary objects contain indices
        print(dict(row))


if __name__ == "__main__": main()
