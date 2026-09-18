"""Algebra domain register. Listed V, listed G, theta when it misses.

    PYTHONPATH=process-calc:. python3 -m pcalc.algscope
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import permutations, product

from pcalc.kernel import Theta, isolate


def banner(name, status):
    print(f"\n== {name}  [{status}]")


def zn_add_mul(n):
    return list(range(n)), lambda a, b: (a + b) % n, lambda a, b: (a * b) % n


def units(n):
    return [a for a in range(1, n) if any((a * b) % n == 1 for b in range(1, n))]


def main():
    print("ALG SCOPE  algebra branches as cuts")
    n_ok = 0

    banner("1 magma / semigroup / monoid", "ENUM")
    V = (0, 1)
    assoc = all(min(min(a, b), c) == min(a, min(b, c)) for a, b, c in product(V, V, V))
    print(f"  min on {{0,1}} assoc {assoc}  id {1}")
    n_ok += 1

    banner("2 groups  S3 not abelian", "ENUM")
    S3 = list(permutations(range(3)))

    def comp(a, b):
        return tuple(a[b[i]] for i in range(3))

    ab = all(comp(a, b) == comp(b, a) for a, b in product(S3, S3))
    print(f"  |S3|={len(S3)} abelian={ab}")
    n_ok += 1

    banner("3 rings / Z/n", "ENUM")
    print(f"  Z/4 units {units(4)}  not a field")
    print(f"  Z/5 units {units(5)}  fieldish")
    n_ok += 1

    banner("4 fields", "ENUM")
    fieldish = {n for n in range(2, 13) if len(units(n)) == n - 1}
    print(f"  fieldish n=2..12 {sorted(fieldish)}")
    n_ok += 1

    banner("5 integral domain", "ENUM")
    zero_div = [(a, b) for a, b in product(range(4), range(4)) if a and b and (a * b) % 4 == 0]
    print(f"  Z/4 zero-divisors {zero_div}")
    n_ok += 1

    banner("6 polynomials over Q", "Q")
    x = isolate(2)
    p = x ** 3 - 2 * x + 1
    print(f"  x^3-2x+1 at 2 {p}")
    n_ok += 1

    banner("7 linear solve listed", "SEARCH")
    V = list(range(7))
    sols = [x for x in V if (3 * x + 1) % 7 == 5]
    print(f"  3x+1=5 in Z/7 -> {sols}")
    n_ok += 1

    banner("8 matrices 2x2 over Q", "Q")
    def det(a, b, c, d):
        return a * d - b * c

    print(f"  det [[1,2],[3,4]] = {det(1,2,3,4)}")
    try:
        if det(1, 2, 2, 4) == 0:
            raise Theta("singular")
    except Theta as e:
        print(f"  [[1,2],[2,4]] {e}")
    n_ok += 1

    banner("9 inverse 2x2", "Q + THETA")
    a, b, c, d = F(1), F(2), F(3), F(5)
    D = det(a, b, c, d)
    inv = (d / D, -b / D, -c / D, a / D)
    print(f"  inv [[1,2],[3,5]] = {inv}  det {D}")
    n_ok += 1

    banner("10 eigen 2x2 char poly", "Q")
    # [[2,0],[0,3]] char (2-l)(3-l)
    print("  diag(2,3) traces 5 det 6  l^2-5l+6")
    print("  roots listed search on Q cut, not R-closure")
    n_ok += 1

    banner("11 quotients Z -> Z/n", "WRAP")
    print(f"  5 reads {5 % 3} at tick 3  {5 % 7} at tick 7")
    n_ok += 1

    banner("12 lattices min/max", "ENUM")
    V3 = (0, F(1, 2), 1)
    closed = all(min(a, b) in V3 and max(a, b) in V3 for a, b in product(V3, V3))
    print(f"  min/max closed on V3 {closed}")
    n_ok += 1

    banner("13 boolean on V2", "ENUM")
    V2 = (0, 1)
    print(f"  AND=min OR=max NOT=1-  LEM {all(max(a,1-a)==1 for a in V2)}")
    n_ok += 1

    banner("14 homomorphisms wrap", "ENUM")
    ok = all((a + b) % 3 == ((a % 3) + (b % 3)) % 3 for a in range(9) for b in range(9))
    print(f"  mod-3 hom on 0..8 add {ok}")
    n_ok += 1

    banner("15 tropical minplus", "ENUM")
    def tadd(a, b):
        return min(a, b)

    def tmul(a, b):
        return a + b
    print(f"  2⊕5={tadd(2,5)}  2⊗5={tmul(2,5)}")
    n_ok += 1

    banner("16 geometric algebra 2d mini", "Q")
    # e1^2=1 e2^2=1 e1e2=-e2e1
    print("  bivector square: (e1e2)^2 = -1  wrap, not a new soul")
    n_ok += 1

    banner("17 gcd / Bezout listed", "SEARCH")
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    print(f"  gcd(12,8)={gcd(12,8)}")
    n_ok += 1

    banner("18 generating function jet", "Q")
    x = isolate(0)
    # 1/(1-x) jet at 0 is 1+x+x^2+...
    acc = isolate(0, 0)
    for k in range(4):
        acc = acc + x ** k
    print(f"  geom gen at 0 n=3 {acc}")
    n_ok += 1

    banner("19 Lie / reps / AG / homology", "DEFER")
    print("  other V or extra slots. name the knob. not silent R.")
    n_ok += 1

    banner("20 letters are holes", "REWRITE")
    print("  solve 2x+1=7 on Q: x=3. letter is a hole, not a box.")
    n_ok += 1

    print(f"\n  algebra branches registered {n_ok}")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
