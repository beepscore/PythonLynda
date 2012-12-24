#!/usr/local/bin/python3

# isprime() is a helper function.
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

# primes() uses "yield". It's a generator function.
# It returns an iterator object that can be used in a for loop.
def primes(n = 1):
   while(True):
       if isprime(n): yield n
       n += 1 

for n in primes():
    if n > 100: break
    print(n)

