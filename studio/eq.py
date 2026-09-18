"""Priced equality. A=A is a weigh, not a prior.

= is a scale: tick (wrap), drift (maintenance), ledger (weighs).
Free A=A is announcing balance with the pans in the cupboard.

    PYTHONPATH=. python3 -m studio.eq
"""
from __future__ import annotations

from fractions import Fraction as F


class Scale:
    def __init__(self, tick=1):
        self.tick = tick
        self.drift = 0
        self.weighs = 0

    def read(self, w):
        return (w // self.tick) + self.drift

    def match(self, a, b):
        self.weighs += 1
        return self.read(a) == self.read(b)


def priced(a, b, on=("val",)):
    """Match only listed dimensions. Missing field: refuse."""
    for k in on:
        if k not in a or k not in b:
            return False
        if a[k] != b[k]:
            return False
    return True


def main():
    print("EQ  A=A is a weigh")
    print()

    s = Scale(tick=3)
    m55 = s.match(5, 5)
    m52 = s.match(5, 2)
    print(f"  tick=3  5 vs 5 {m55} reads {s.read(5)}")
    print(f"  tick=3  5 vs 2 {m52} reads {s.read(5)} vs {s.read(2)}")
    assert m55 and not m52

    recorded = s.read(5)
    s.drift = 1
    across_time = recorded == s.read(5)
    print(f"  drift=1  recorded {recorded} vs now {s.read(5)}  A=A-across-time {across_time}")
    assert across_time is False

    xx = {"val": (F(9), F(6)), "g": "x2", "slot": F(2)}
    tx = {"val": (F(9), F(6)), "g": "3x", "slot": F(0)}
    free = priced(xx, tx, on=("val",))
    mint = priced(xx, tx, on=("val", "g"))
    slot = priced(xx, tx, on=("val", "slot"))
    print(f"  pair collision free-val {free}  mint {mint}  slot {slot}")
    assert free and (not mint) and (not slot)
    print("  free = plus sub on slot would write 2=0. priced = refuses.")

    # mint-eq on this cut is only loops
    print("  mint-priced = on this cut: two loops, no cross. drop A=A, R empty.")
    print(f"  weighs taken {s.weighs}")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
