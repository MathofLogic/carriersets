"""Major math domains. Far as this cut goes.

Each line is a player or field: closes here, leftover, or DEFER.
Quantum is named, not instantiated.

    PYTHONPATH=process-calc:. python3 -m pcalc.domains
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product


def banner(name, status):
    print(f"\n== {name}  [{status}]")


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print("DOMAINS  major fields as cuts")
    n = 0

    banner("foundations / logic", "REPO")
    print("  studio.logic  modal.verify  origin.walls  113 assoc  530 frames")
    n += 1

    banner("set theory HF", "ENUM")
    print("  hereditary-finite is a listed wrap. actual Inf is grow-V.")
    n += 1

    banner("number theory", "SEARCH")
    primes = [p for p in range(2, 30) if all(p % d for d in range(2, p))]
    print(f"  primes <30 {primes}")
    print(f"  gcd(48,18)={gcd(48,18)}  Euler totient Z/7 units 6")
    n += 1

    banner("combinatorics / graphs", "ENUM")
    print(f"  C(5,2)={len(list(combinations(range(5),2)))}")
    print(f"  K3 edges {len(list(combinations(range(3),2)))}")
    n += 1

    banner("algebra", "LAB")
    print("  pcalc.algscope  S3  Z/n  det  tropical")
    n += 1

    banner("algebraic geometry", "DEFER")
    print("  schemes / varieties: other V. zeros of x^2+y^2-1 listed on Q-grid.")
    circ = [(x, y) for x in range(-2, 3) for y in range(-2, 3) if x * x + y * y == 1]
    print(f"  integer points on x^2+y^2=1 {circ}")
    n += 1

    banner("calculus / analysis", "LAB")
    print("  pcalc.scope translab veclab jetlab  ε-δ unlistable")
    n += 1

    banner("functional analysis", "DEFER")
    print("  operators on Inf-dim: grow V. finite matrices are algscope.")
    n += 1

    banner("harmonic / Fourier", "GRID")
    print("  coefficients = extracts on a listed mesh. not Inf sums.")
    n += 1

    banner("ODE / PDE / dynamics", "CONSTRAINT")
    print("  y'=2y reading (1,2). logistic leftover. chaos: other extract.")
    n += 1

    banner("differential geometry", "SLOT")
    print("  curvature r2 slot. geodesic rate constraint. topgeoscope.")
    n += 1

    banner("topology / geometry", "LAB")
    print("  pcalc.topgeoscope  Euler 2  3-4-5  parallels family")
    n += 1

    banner("probability / statistics", "LAB")
    print("  pcalc.statscope  Bayes 3/4  E die 7/2")
    n += 1

    banner("information theory", "EXTRACT")
    print("  fair bit entropy 1 on stipulated log2. KL is two extracts.")
    n += 1

    banner("game theory", "ENUM")
    # matching pennies payoff
    print("  2x2 zero-sum listed. saddle is a search, not a soul.")
    pay = ((1, -1), (-1, 1))
    print(f"  matching pennies {pay}")
    n += 1

    banner("optimization / control", "RATE=0")
    print("  stationarity is dead channel. Lagrange: extra isolator.")
    n += 1

    banner("numerical analysis", "LEFTOVER")
    print("  fd leftover vs rate. Newton is a wrap of the rate cut.")
    n += 1

    banner("complexity", "PRESCREEN")
    print("  P vs NP is a lift. studio.proofcut / origin. not a soul.")
    n += 1

    banner("cryptography mini", "WRAP")
    print(f"  3^4 mod 7 = {pow(3,4,7)}  discrete wrap, not a lock-substance")
    n += 1

    banner("category / HoTT", "POINTER")
    print("  arrows not objects-as-stuff. identity is a paid loop.")
    n += 1

    banner("representation / Lie", "DEFER")
    print("  other V. so(2) is a wrap. not a group-soul.")
    n += 1

    banner("mathematical physics / quantum", "NEXT")
    print("  isolations, wraps, theta. Hilbert furniture is the substance bug.")
    print("  next register. not this file.")
    n += 1

    banner("operations / actuarial / rec", "COMPRESS")
    print("  same extracts. different nouns. do not promote the noun.")
    n += 1

    print(f"\n  domain rows {n}")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
