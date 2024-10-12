import functools
from collections.abc import Iterator
from math import sqrt
from time import time

import numpy as np
from numpy import ndarray


def time_func(func, *args, **kwargs):
    """
    Times the execution of a function with parameters
    """
    start = time()  # Începe măsurarea timpului
    output = func(*args, **kwargs)  # Apelează funcția dată și obține rezultatul
    end = time()  # Încheie măsurarea timpului

    # Afișează timpul de execuție
    if int(end - start) > 0:
        print(f"{func.__name__} runtime: {(end - start):0.4f} s")
    else:
        print(f"{func.__name__} runtime: {(end - start) * 1000:0.4f} ms")

    # Afișează rezultatul calculat
    print(f"Result from {func.__name__}: {output}")

    return output


# Exemple de funcții Fibonacci pentru testare
def fib_iterative(n: int) -> list[int]:
    """Calculates the first n Fibonacci numbers using iteration."""
    if n == 0:
        return [0]
    fib = [0, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return fib


def fib_binet(n: int) -> list[int]:
    """Calculates Fibonacci numbers using Binet's formula (approximative)."""
    sqrt_5 = sqrt(5)
    phi = (1 + sqrt_5) / 2
    return [round(phi ** i / sqrt_5) for i in range(n + 1)]


# Testarea funcțiilor Fibonacci și măsurarea timpului de execuție
if __name__ == "__main__":
    num = 10  # Numărul de termeni Fibonacci pe care vrem să îi generăm

    # Apelăm funcțiile și măsurăm timpul de execuție pentru fiecare
    time_func(fib_iterative, num)
    time_func(fib_binet, num)
