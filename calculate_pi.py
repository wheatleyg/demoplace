#!/usr/bin/env python3
"""
Calculate Pi using various algorithms
"""
import math
import random
import time


def leibniz_formula(iterations=1000000):
    """
    Calculate pi using the Leibniz formula:
    π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    
    Simple but slow convergence.
    """
    pi = 0
    for i in range(iterations):
        pi += ((-1) ** i) / (2 * i + 1)
    return pi * 4


def monte_carlo_method(iterations=1000000):
    """
    Calculate pi using Monte Carlo simulation.
    
    Randomly place points in a unit square and count how many
    fall inside a quarter circle. The ratio approximates π/4.
    """
    inside_circle = 0
    for _ in range(iterations):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
    return 4 * inside_circle / iterations


def nilakantha_series(iterations=1000):
    """
    Calculate pi using the Nilakantha series:
    π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
    
    Faster convergence than Leibniz.
    """
    pi = 3
    sign = 1
    for i in range(2, iterations * 2, 2):
        pi += sign * 4 / (i * (i + 1) * (i + 2))
        sign *= -1
    return pi


def chudnovsky_algorithm(iterations=2):
    """
    Calculate pi using the Chudnovsky algorithm.
    
    Very fast convergence - each term adds about 14 digits of precision.
    """
    k = 0
    pi = 0
    for k in range(iterations):
        numerator = ((-1) ** k) * math.factorial(6 * k) * (545140134 * k + 13591409)
        denominator = math.factorial(3 * k) * (math.factorial(k) ** 3) * (640320 ** (3 * k))
        pi += numerator / denominator
    
    pi = pi * 12 / (640320 ** 1.5)
    return 1 / pi


def machin_formula():
    """
    Calculate pi using Machin's formula:
    π/4 = 4*arctan(1/5) - arctan(1/239)
    
    Fast and accurate.
    """
    return 4 * (4 * math.atan(1/5) - math.atan(1/239))


def main():
    print("=" * 60)
    print("Pi Calculation using Various Algorithms")
    print("=" * 60)
    print(f"\nActual value of π: {math.pi}\n")
    
    methods = [
        ("Leibniz Formula (1M iterations)", lambda: leibniz_formula(1000000)),
        ("Monte Carlo Method (1M iterations)", lambda: monte_carlo_method(1000000)),
        ("Nilakantha Series (10K iterations)", lambda: nilakantha_series(10000)),
        ("Chudnovsky Algorithm (3 iterations)", lambda: chudnovsky_algorithm(3)),
        ("Machin's Formula", machin_formula),
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method()
        elapsed_time = time.time() - start_time
        error = abs(result - math.pi)
        
        print(f"{name}:")
        print(f"  Result: {result:.15f}")
        print(f"  Error:  {error:.15e}")
        print(f"  Time:   {elapsed_time:.4f} seconds")
        print()


if __name__ == "__main__":
    main()
