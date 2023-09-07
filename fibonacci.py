# Implementations of Fibonacci sequence
from time import time


def fibonacci(n):
    if n in {0, 1}:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


cache = {0: 0, 1: 1}


def fibonacci_caching(n):
    if n not in cache:
        cache[n] = fibonacci_caching(n - 1) + fibonacci_caching(n - 2)
    return cache[n]


t1 = time()
sequence = [fibonacci_caching(n) for n in range(10000)]
t2 = time()
print(sequence)
print("Elapsed time", t2-t1, "seconds")
