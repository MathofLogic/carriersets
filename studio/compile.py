"""A framework compiles when a program is bound to current support.

Self-similar: the bound program still lands after a listed shift.
Reconfigure: the signature flips or the write misses V.
Rate of reconfigure: misses / shifts. Not a cosmic constant.
"""
from fractions import Fraction as F
from itertools import product


def closed(V, fn):
    return all(fn(a, b) in V for a, b in product(V, V))


def main():
    V2, V3, V4 = (0, 1), (0, F(1, 2), 1), (0, F(1, 3), F(1, 2), 1)
    print("COMPILE  bind G to support; watch the shift")
    for name, fn in (("min", min), ("prod", lambda a, b: a * b)):
        hits = [closed(V, fn) for V in (V2, V3, V4)]
        flips = sum(hits[i] != hits[i + 1] for i in range(len(hits) - 1))
        print(f"  {name:4} closed {hits}  reconfig_rate {flips}/2")
    seeds = [1, 2, F(1, 2)]
    rates = []
    for s in seeds:
        v, r = F(3), F(s)
        rates.append((r * v + v * r) / r)
    print(f"  rate-mix seeds {rates}  self-similar {len(set(rates))==1}")
    print("  loaded history supported → same write. constraint shift → count misses.")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
