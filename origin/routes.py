"""Two routes. They agree on a cut. They do not escape stipulation."""
import json
import os
import sys

from claims import Suite
from closure import Closure, co_propagate, iterate
from peano_carrier import S, add, mul, nat


def m_add(a, b):
    C = Closure(max(a + b, 1) + 1)
    return co_propagate(C, a, b)


def m_mul(a, b):
    C = Closure(max(a * b, 1) + 1)
    return iterate(C, a, b)


def m_succ(a):
    return m_add(a, 1)


def p_add(a, b):
    return int(add(nat(a), nat(b)))


def p_mul(a, b):
    return int(mul(nat(a), nat(b)))


def p_succ(a):
    return int(S(nat(a)))


def audit():
    S = Suite("ROUTES — two presentations, one wall", __file__)
    N = range(0, 9)
    succ_ok = all(m_succ(a) == p_succ(a) for a in N)
    S.add("successor agrees on {0..8}", succ_ok, len(N), len(N), True,
          "exhibit k in 0..8 where wrap-succ and Peano-succ split",
          "{0..8}")

    pairs = [(a, b) for a in N for b in N]
    add_ok = all(m_add(a, b) == p_add(a, b) for a, b in pairs)
    mul_ok = all(m_mul(a, b) == p_mul(a, b) for a, b in pairs)
    S.add("addition agrees on 81 pairs", add_ok, 81, 81, True,
          "exhibit a pair in 0..8 where the two + split", "81 pairs")
    S.add("multiplication agrees on 81 pairs", mul_ok, 81, 81, True,
          "exhibit a pair in 0..8 where the two * split", "81 pairs")

    S.add("mechanism route still calls host + inside co_propagate",
          True, 1, 1, True,
          "implement m_add with no host addition",
          "source", derived=False)
    S.add("neither route certifies unbounded + from this cut",
          True, 0, None, False,
          "exhibit a finite check that closes + on all Nat without a schema",
          derived=True)

    S.nonclaim("NOT claimed: mechanism assumes nothing. It assumes a wrap.")
    S.nonclaim("NOT claimed: agreement on 81 pairs is Peano arithmetic.")
    return S


if __name__ == "__main__":
    Su = audit()
    Su.report()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "manifests", "routes_manifest.json"), "w") as f:
        json.dump(Su.manifest(), f, indent=2, sort_keys=True)
    sys.exit(1 if Su.failed() else 0)
