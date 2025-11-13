#!/usr/bin/env python3

def print_fibonacci(n):
    """Print the first n Fibonacci numbers as a list: [0, 1, 1, …]"""
    if n <= 0:
        print("[]")
        return

    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    # Build the required string: "[0, 1, 1, ...]"
    print("[" + ", ".join(map(str, fib)) + "]")