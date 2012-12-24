#!/usr/local/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():
    # __init__() is a constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # series() is a generator
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

# instantiate an instance of class Fibonacci.
f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break    
    print(r, end=' ')

