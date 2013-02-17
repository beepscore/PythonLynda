#!/usr/bin/env python3

# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# Python comes with sqlite
# sqlite is simple to use. Doesn't require setting up a server
# mySQL requires setting up a server.
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

    db = sqlite3.connect('test.sqlite')
    # delete old table
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    db.commit()
    cursor = db.execute('select * from test order by t1')

    for row in cursor:
        print(row)


if __name__ == "__main__": main()
