"""Numbers a skeptic can rerun. If these move, the README is a lie."""
from __future__ import annotations

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from fractions import Fraction as F

from pl import LeavesV, certify, isolate, rate


def check(name, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    return ok


def main():
    bad = 0
    x = isolate(3)
    bad += not check("rate(x*x, x) at 3 is 6", rate(x * x, x) == 6)
    for seed in (1, 2, F(1, 2), 10, -1):
        xs = isolate(3, seed)
        bad += not check(f"gauge seed={seed}", rate(xs * xs, xs) == 6)
    c = certify(lambda z: z * z, at=3)
    bad += not check("certify x*x FORCED-on-cut 32/32", c.ok and c.discharged == 32)
    try:
        isolate(3.0)
        bad += not check("float leaves V", False)
    except LeavesV:
        bad += not check("float leaves V", True)
    a = isolate(3, 1) * isolate(3, 1)  # x^2 seed 1
    b = isolate(3, 2) * 3              # 3x seed 2
    bad += not check("collision (9,6) from x^2 and 3x", (a.v, a.r) == (b.v, b.r) == (F(9), F(6)))

    from mechanism.traveler import time_to, until_theta
    bad += not check("arrivals 50,150,450", (time_to(0), time_to(2), time_to(8)) == (50, 150, 450))
    tick, tr = until_theta(0.5, 12.0)
    bad += not check("theta 12 at tick 167", tick == 167)

    from studio.logic import assoc
    from itertools import product
    V3 = (0, 1, 2)
    n_assoc = 0
    for cells in product(V3, repeat=9):
        fn = lambda a, b, cells=cells: cells[a * 3 + b]
        if assoc(V3, fn):
            n_assoc += 1
    bad += not check("V3 assoc=113", n_assoc == 113)
    bad += not check("|Bin(V3)|=19683", 3 ** 9 == 19683)

    from modal.engine import all_frames
    n = len(list(all_frames(3)))
    bad += not check("frames n<=3 = 530", n == 530)

    print("SKEPTIC", "PASSED" if bad == 0 else f"FAILED {bad}")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
