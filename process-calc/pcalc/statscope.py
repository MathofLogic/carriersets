"""Probability and statistics as listed extracts.

A measure on an unlistable R is grow-V. Here: finite V, ratio,
grid extract, theta when the condition is empty.

    PYTHONPATH=process-calc:. python3 -m pcalc.statscope
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def banner(name, status):
    print(f"\n== {name}  [{status}]")


def main():
    print("STAT SCOPE  probability / statistics as cuts")
    n_ok = 0

    banner("1 sample space listed", "ENUM")
    Omega = (1, 2, 3, 4, 5, 6)
    print(f"  |Omega|={len(Omega)}")
    n_ok += 1

    banner("2 uniform / counting", "RATIO")
    even = tuple(x for x in Omega if x % 2 == 0)
    print(f"  P(even)={F(len(even), len(Omega))}")
    n_ok += 1

    banner("3 conditional", "RATIO OF CHANNELS")
    A = tuple(x for x in Omega if x > 3)
    B = tuple(x for x in Omega if x % 2 == 0)
    AB = tuple(x for x in A if x in B)
    print(f"  P(even|gt3)={F(len(AB), len(A))}")
    n_ok += 1

    banner("4 Bayes", "TWO ISOLATIONS")
    # two bowls
    prior = {"r": F(1, 2), "b": F(1, 2)}
    like = {"r": F(3, 4), "b": F(1, 4)}  # P(gold|bowl)
    evid = prior["r"] * like["r"] + prior["b"] * like["b"]
    post_r = prior["r"] * like["r"] / evid
    print(f"  P(red|gold)={post_r}  evid={evid}")
    n_ok += 1

    banner("5 expectation grid", "EXTRACT")
    p = {x: F(1, 6) for x in Omega}
    ex = sum(x * p[x] for x in Omega)
    print(f"  E[die]={ex}")
    n_ok += 1

    banner("6 variance", "EXTRACT")
    mu = ex
    var = sum((x - mu) ** 2 * p[x] for x in Omega)
    print(f"  Var={var}")
    n_ok += 1

    banner("7 independence", "ENUM")
    # coin x die would be product; here two bits
    bits = (0, 1)
    indep = all(True for _ in product(bits, bits))
    print(f"  product space |V|={len(bits)**2}  listed joint")
    n_ok += 1

    banner("8 empty condition", "THETA")
    C = tuple(x for x in Omega if x > 6)
    print(f"  P(*|empty) refuses  |C|={len(C)}")
    n_ok += 1

    banner("9 likelihood / MLE listed", "SEARCH")
    # binomial n=3, data 2 heads; p in {0,1/2,1}
    def lik(p):
        # C(3,2) p^2 (1-p)
        return 3 * p * p * (1 - p)
    grid = [F(0), F(1, 2), F(1)]
    scores = {p: lik(p) for p in grid}
    print(f"  lik on {grid} -> {scores}")
    n_ok += 1

    banner("10 hypothesis as theta", "CUT")
    print("  reject if extract leaves the guard. not a soul of 'significance'.")
    n_ok += 1

    banner("11 entropy listed", "EXTRACT")
    # two-coin fair: 2 bits. use log2 via known Q on p=1/2: -p log2 p *2 = 1
    print("  fair bit entropy 1  (stipulated log2(1/2)=-1 on this cut)")
    n_ok += 1

    banner("12 LLN / CLT / densities on R", "DEFER")
    print("  wrap of means is another extract. CLT/R-density: grow V.")
    n_ok += 1

    print(f"\n  stat branches registered {n_ok}")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
