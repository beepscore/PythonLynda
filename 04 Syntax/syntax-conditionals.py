#!/usr/local/bin/python3

def main():
    a, b = 5, 1
    # conditional expression
    if a == b:
        print('a:{} equals b:{}'.format(a, b))
    elif a < b:
        print('a:{} is less than b:{}'.format(a, b))
    else:
        print('a:{} is greater than b:{} or they don\'t compare'.format(a, b))

    # conditional assignment
    s = "less than" if a < b else "not less than"
    # I think an earlier version of python 3 (3.1?) required number inside {}. 3.2 doesn't need it.
    # print("a is {0} b".format(s))
    print("a is {} b".format(s))

if __name__ == "__main__": main()
