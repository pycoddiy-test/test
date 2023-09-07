# Implementations of Fibonacci sequence
from time import time


def fibonacci(n):
    if n in {0, 1}:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


t1 = time()
sequence = [fibonacci(n) for n in range(35)]
t2 = time()
print(sequence)
print("Elapsed time", t2-t1, "seconds")
