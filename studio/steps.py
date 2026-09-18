"""steps.py — operations to output, counted.

Claim: rate(x*x, x) at 3 reaches 6 with a finite arithmetic list.
The school limit path reaches 6+h with a finite list, then imports
a limit step that this V does not contain.

    PYTHONPATH=. python3 -m studio.steps

Falsifier: exhibit a finite arithmetic list, using only + * / on Q
and no limit/Inf/cancel-by-fiat, that turns (f(3+h)-f(3))/h into 6
for a generic h.
"""
from __future__ import annotations

from fractions import Fraction as F


class Tape:
    def __init__(self, name):
        self.name = name
        self.ops = []
        self.value = None

    def add(self, a, b):
        self.ops.append(("+", a, b, a + b))
        return a + b

    def sub(self, a, b):
        self.ops.append(("-", a, b, a - b))
        return a - b

    def mul(self, a, b):
        self.ops.append(("*", a, b, a * b))
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("theta")
        self.ops.append(("/", a, b, a / b))
        return a / b

    def n(self):
        return len(self.ops)


def pair_square_rate(at=F(3), seed=F(1)):
    t = Tape("pair")
    v, r = at, seed
    vv = t.mul(v, v)
    vr = t.mul(v, r)
    rv = t.mul(r, v)
    rr = t.add(vr, rv)
    out = t.div(rr, r)
    t.value = out
    return t


def fd_square(at=F(3), h=F(1, 2)):
    t = Tape("fd")
    three_h = t.add(at, h)
    sq1 = t.mul(three_h, three_h)
    sq0 = t.mul(at, at)
    diff = t.sub(sq1, sq0)
    out = t.div(diff, h)
    t.value = out
    return t


def school_cancel(at=F(3), h=F(1, 2)):
    """Algebra to 6+h. Does not delete h."""
    t = Tape("school-to-6+h")
    three_h = t.add(at, h)
    sq1 = t.mul(three_h, three_h)
    sq0 = t.mul(at, at)
    diff = t.sub(sq1, sq0)
    q = t.div(diff, h)
    t.value = q
    return t


def main():
    p = pair_square_rate()
    f = fd_square()
    s = school_cancel()
    print("OPS TO OUTPUT  f = x^2 at x=3")
    print()
    print(f"  pair rate          ops={p.n()}  value={p.value}")
    for op in p.ops:
        print(f"    {op[0]}  {op[1]} {op[2]} -> {op[3]}")
    print()
    print(f"  fd h=1/2           ops={f.n()}  value={f.value}  leftover={f.value - 6}")
    print(f"  school to 6+h      ops={s.n()}  value={s.value}")
    print()
    print("  step the school path still owes: delete h.")
    print("  that step is not + * / on Q. it is an imported limit/fiat.")
    print("  pair path owes no such step. output is 6.")
    print()
    print(f"  check: pair==6 {p.value==6}  fd==6 {f.value==6}  school==6 {s.value==6}")
    print("verdict", "PASS" if p.value == 6 and f.value != 6 else "FAIL")
    return 0 if p.value == 6 and f.value != 6 else 1


if __name__ == "__main__":
    raise SystemExit(main())
