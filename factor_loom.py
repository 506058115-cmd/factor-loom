#!/usr/bin/env python3
"""Print the prime factorization of a bounded nonzero integer."""

import argparse


MAX_ABS_VALUE = 1_000_000_000_000


def factorize(value):
    factors = ["-1"] if value < 0 else []
    remainder = abs(value)
    divisor = 2
    # ponytail: trial division is capped at 10^12; use Pollard rho if larger inputs matter.
    while divisor * divisor <= remainder:
        exponent = 0
        while remainder % divisor == 0:
            remainder //= divisor
            exponent += 1
        if exponent:
            factors.append(f"{divisor}^{exponent}" if exponent > 1 else str(divisor))
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        factors.append(str(remainder))
    return factors or ["1"]


def main():
    parser = argparse.ArgumentParser(description="Show a prime factorization for an integer up to 10^12 in magnitude.")
    parser.add_argument("number", type=int, help="nonzero decimal integer")
    args = parser.parse_args()
    if args.number == 0:
        parser.error("zero has no finite prime factorization")
    if abs(args.number) > MAX_ABS_VALUE:
        parser.error("absolute value must be at most 1000000000000")
    print(" * ".join(factorize(args.number)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
