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
    # Python 3.0 required positional or name indicator number inside {}.
    # >= 3.1 will just infer from order. You can change order using positional indicator or name.
    # print("a is {0} b".format(s))
    print("a is {} b".format(s))

if __name__ == "__main__": main()
