#!/usr/bin/env python3
"""Approximate the value of π using the Nilakantha series.

The Nilakantha series converges faster than the Leibniz series and is
defined as:

    π = 3 + Σ_{n=1..∞} (-1)^{n+1} * 4 / ((2n)(2n+1)(2n+2))

Run this script with an optional ``--iterations`` argument to control how
many terms of the series are summed. More iterations lead to a more
accurate approximation, but increase compute time.
"""

from __future__ import annotations

import argparse
import math
from typing import Iterable


def nilakantha_series(iterations: int) -> Iterable[float]:
    """Yield successive terms of the Nilakantha series."""

    for n in range(1, iterations + 1):
        numerator = 4.0
        denominator = (2.0 * n) * (2.0 * n + 1.0) * (2.0 * n + 2.0)
        sign = 1.0 if n % 2 else -1.0
        yield sign * numerator / denominator


def approximate_pi(iterations: int) -> float:
    """Return an approximation of π using ``iterations`` Nilakantha terms."""

    return 3.0 + sum(nilakantha_series(iterations))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n",
        "--iterations",
        type=int,
        default=100000,
        help="number of terms to sum (default: %(default)s)",
    )
    parser.add_argument(
        "--show-error",
        action="store_true",
        help="display the absolute error versus math.pi",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.iterations < 1:
        raise SystemExit("iterations must be a positive integer")

    approximation = approximate_pi(args.iterations)
    print(f"π ≈ {approximation:.15f}")

    if args.show_error:
        error = abs(math.pi - approximation)
        print(f"absolute error: {error:.3e}")


if __name__ == "__main__":
    main()
