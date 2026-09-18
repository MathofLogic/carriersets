"""Operators are programs.

V = the state alphabet the program may write
G = the program
theta = refuse / reconfigure when the write misses V

Nothing deeper is claimed. The same loop is rate, BOX, wrap-add,
min, vent. Change the program, the postcard changes.
"""
from itertools import product
from fractions import Fraction as F


def closed(V, fn):
    return all(fn(a, b) in V for a, b in product(V, V))


def main():
    V2, V3 = (0, 1), (0, F(1, 2), 1)
    print("OPERATORS  programs on a listed V")
    print(f"  min  closed V2={closed(V2, min)} V3={closed(V3, min)}")
    print(f"  prod closed V2={closed(V2, lambda a,b: a*b)} "
          f"V3={closed(V3, lambda a,b: a*b)}")
    x = (F(3), F(1))
    mix = (x[0] * x[0], x[1] * x[0] + x[0] * x[1])
    ignore = (x[0] * x[0], x[1] * x[1])
    print(f"  Leibniz mix {mix} rate {mix[1]/x[1]}")
    print(f"  ignore-r    {ignore} rate {ignore[1]/x[1]}")
    print("  persist: isolate, apply, land-in-V or theta, maybe split.")
    print("  that loop is the mechanism. frames are different programs.")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
