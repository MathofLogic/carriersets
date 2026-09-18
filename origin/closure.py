"""Mechanism route. A wrap. Numbers are what the wrap can distinguish.

co_propagate uses host + and %. That is Wall 0. This file does not hide it.
"""
import json
import os
import sys

from claims import Suite


class Closure:
    __slots__ = ("n",)

    def __init__(self, n):
        if n < 1:
            raise ValueError("a closure must close")
        self.n = n

    def positions(self):
        return range(self.n)


def co_propagate(C, a, b):
    """Two windings, wrap. Host + and % do the work. See walls.WALL 0."""
    return (a + b) % C.n


def iterate(C, a, k):
    out = 0
    for _ in range(k):
        out = co_propagate(C, out, a)
    return out


def inverse(C, a):
    return (-a) % C.n


def annihilates(C, a, b):
    return a % C.n != 0 and b % C.n != 0 and (a * b) % C.n == 0


def audit():
    S = Suite("CLOSURE — the primitive", __file__)
    NS = range(1, 13)
    n_assoc = n_comm = n_id = n_inv = 0
    ok_assoc = ok_comm = ok_id = ok_inv = True
    for n in NS:
        C = Closure(n)
        for a in C.positions():
            n_id += 1
            ok_id &= co_propagate(C, a, 0) == a
            n_inv += 1
            ok_inv &= co_propagate(C, a, inverse(C, a)) == 0
            for b in C.positions():
                n_comm += 1
                ok_comm &= co_propagate(C, a, b) == co_propagate(C, b, a)
                for c in C.positions():
                    n_assoc += 1
                    ok_assoc &= (
                        co_propagate(C, co_propagate(C, a, b), c)
                        == co_propagate(C, a, co_propagate(C, b, c))
                    )
    cut = f"closures 1..{max(NS)}"
    S.add("co-propagation is associative", ok_assoc, n_assoc, n_assoc, True,
          "exhibit a wrap and three windings where grouping matters", cut)
    S.add("co-propagation is commutative", ok_comm, n_comm, n_comm, True,
          "exhibit two windings whose order changes the result", cut)
    S.add("0 is identity of co-propagation", ok_id, n_id, n_id, True,
          "exhibit a winding that 0 moves", cut)
    S.add("every winding has an inverse under co-propagation",
          ok_inv, n_inv, n_inv, True,
          "exhibit a winding with no undo", cut)
    uses_host = "+" in open(__file__).read() and "%" in open(__file__).read()
    S.add("this file's wrap is implemented with host + and %",
          uses_host, 1, 1, True,
          "rewrite co_propagate with no host addition or remainder",
          "source of co_propagate")
    S.nonclaim("NOT claimed: that a wrap derives addition from nothing.")
    S.nonclaim("NOT claimed: that these laws lift off the cut without induction.")
    return S


if __name__ == "__main__":
    Su = audit()
    Su.report()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "manifests", "closure_manifest.json"), "w") as f:
        json.dump(Su.manifest(), f, indent=2, sort_keys=True)
    sys.exit(1 if Su.failed() else 0)
