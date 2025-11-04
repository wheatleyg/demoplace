#!/usr/bin/env python3
"""Compute an arbitrary-precision approximation of pi using the Gauss-Legendre algorithm.

Usage:
    python pi_solver.py --digits 1000

The algorithm converges quadratically, so each iteration roughly doubles the
number of correct digits. This script stops when the arithmetic mean and
geometric mean agree to the requested precision.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext


def gauss_legendre_pi(digits: int) -> Decimal:
    """Return pi rounded to *digits* decimal places using Gauss-Legendre."""

    if digits <= 0:
        raise ValueError("digits must be a positive integer")

    extra_precision = 10

    with localcontext() as ctx:
        ctx.prec = digits + extra_precision

        a = Decimal(1)
        b = Decimal(1) / Decimal(2).sqrt()
        t = Decimal("0.25")
        p = Decimal(1)

        threshold = Decimal(10) ** (-(digits + 2))

        while True:
            a_next = (a + b) / 2
            b = (a * b).sqrt()
            t -= p * (a - a_next) ** 2
            a = a_next
            p *= 2

            pi_estimate = ((a + b) ** 2) / (4 * t)

            if abs(a - b) < threshold:
                break

        ctx.prec = digits
        return +pi_estimate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute pi to an arbitrary number of decimal digits using the Gauss-Legendre algorithm.",
    )
    parser.add_argument(
        "-d",
        "--digits",
        default=50,
        type=int,
        help="number of decimal digits to compute (default: 50)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pi_value = gauss_legendre_pi(args.digits)
    print(f"pi ≈ {pi_value}")


if __name__ == "__main__":
    main()
