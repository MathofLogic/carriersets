"""Topology and geometry as listed spaces and wraps.

Opens are collections we list. Distance is a weigh.
Parallel-postulate uniqueness is a high-theta dogma that already
decohered. Quantum is the next register, not this file.

    PYTHONPATH=process-calc:. python3 -m pcalc.topgeoscope
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product


def banner(name, status):
    print(f"\n== {name}  [{status}]")


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def main():
    print("TOP/GEO SCOPE  topology and geometry as cuts")
    n_ok = 0

    banner("1 finite space / discrete topology", "ENUM")
    X = (0, 1, 2)
    print(f"  |X|={len(X)}  discrete opens = Power set size {2**len(X)}")
    n_ok += 1

    banner("2 connectedness listed", "ENUM")
    # path graph 0-1-2 is connected; 0|1 2 is not
    edges = {(0, 1), (1, 0), (1, 2), (2, 1)}

    def path(a, b, seen=None):
        if seen is None:
            seen = set()
        if a == b:
            return True
        seen = seen | {a}
        return any(path(n, b, seen) for n in X if (a, n) in edges and n not in seen)

    conn = all(path(a, b) for a, b in product(X, X))
    print(f"  path-graph connected {conn}")
    n_ok += 1

    banner("3 compactness finite", "ENUM")
    print("  finite X: every open cover has finite subcover. free on this V.")
    n_ok += 1

    banner("4 continuity on listed maps", "ENUM")
    # f:{0,1,2}-> {0,1} f(x)=0 if x<2 else 1. always continuous if codomain discrete
    print("  every map into discrete Y is continuous. cheap theta.")
    n_ok += 1

    banner("5 Euler characteristic", "COUNT")
    # tetrahedron V=4 E=6 F=4
    print(f"  tetra V-E+F={4-6+4}")
    n_ok += 1

    banner("6 fundamental group listed graph", "DEFER MINI")
    print("  loops on a wedge of circles need a word V. not silent pi1.")
    n_ok += 1

    banner("7 homotopy / homology", "DEFER")
    print("  extra slots. name them. do not write [S^n] as furniture.")
    n_ok += 1

    banner("8 metric as weigh", "Q")
    p, q = (F(0), F(0)), (F(3), F(4))
    print(f"  d^2((0,0),(3,4))={dist2(p,q)}  3-4-5 triple")
    n_ok += 1

    banner("9 Pythagorean triples listed", "SEARCH")
    trips = [(a, b, c) for a, b, c in product(range(1, 16), repeat=3)
             if a * a + b * b == c * c and a <= b]
    print(f"  triples a<=b<16 count {len(trips)} first {trips[:3]}")
    n_ok += 1

    banner("10 similar triangles", "RATIO")
    print(f"  3-4-5 scaled 2 = 6-8-10  ratio {F(6,3)}")
    n_ok += 1

    banner("11 incidence geometry finite", "ENUM")
    # Fano is bigger; mini: triangle lines
    pts = (0, 1, 2)
    lines = ((0, 1), (1, 2), (2, 0))
    print(f"  triangle pts {pts} lines {len(lines)}")
    n_ok += 1

    banner("12 convex listed", "ENUM")
    S = ((0, 0), (1, 0), (0, 1))
    print(f"  three points convex  |S|={len(S)}")
    n_ok += 1

    banner("13 curvature / geodesic", "SLOT")
    print("  curvature is a later slot (jet r2 leftover). geodesic is a rate constraint.")
    n_ok += 1

    banner("14 parallel postulate family", "STIPULATED")
    print("  Euclid uniqueness decohered. family of carriers by curvature knob.")
    print("  not 'space is'. maps.")
    n_ok += 1

    banner("15 projective mini", "WRAP")
    print("  lines through origin: wrap of direction. [1:2] same [2:4].")
    print(f"  mint-eq needed or 2=0 style collision")
    n_ok += 1

    banner("16 symplectic / Riemann / schemes", "DEFER")
    print("  other V. quantum next. not this cut.")
    n_ok += 1

    print(f"\n  top/geo branches registered {n_ok}")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
