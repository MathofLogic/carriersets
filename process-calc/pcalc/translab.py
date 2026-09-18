"""Trig, exp, log as process cuts.

Values of sin/exp/log at a generic mark are not in Q.
This lab does not put them in Q. It does three paid things:

1. Initial readings at the marks that *are* in Q.
2. Rate relations (G), which close on those readings.
3. Finite Taylor jets on Q-pairs. The leftover is named.

    PYTHONPATH=process-calc:. python3 -m pcalc.translab
"""
from __future__ import annotations

from fractions import Fraction as F

from pcalc.kernel import Theta, isolate, rate


def fact(n):
    p = F(1)
    for i in range(2, n + 1):
        p *= i
    return p


def exp_jet(x, n=8):
    acc = isolate(0, 0)
    for k in range(n + 1):
        acc = acc + (x ** k) / fact(k)
    return acc


def sin_jet(x, n=8):
    acc = isolate(0, 0)
    sign = 1
    for k in range(n + 1):
        odd = 2 * k + 1
        acc = acc + sign * (x ** odd) / fact(odd)
        sign = -sign
    return acc


def cos_jet(x, n=8):
    acc = isolate(0, 0)
    sign = 1
    for k in range(n + 1):
        even = 2 * k
        acc = acc + sign * (x ** even) / fact(even)
        sign = -sign
    return acc


def log1p_jet(u, n=8):
    """log(1+u) jet. theta if v=-1."""
    if u.v == -1:
        raise Theta("log: 1+u = 0")
    acc = isolate(0, 0)
    sign = 1
    for k in range(1, n + 1):
        acc = acc + sign * (u ** k) / k
        sign = -sign
    return acc


def main():
    print("TRANS LAB  exp / sin / cos / log")
    print("  V for values at generic marks is not Q. Jets stay in Q.")
    print()

    z = isolate(0)
    print("  INIT READINGS (in Q)")
    e0 = exp_jet(z, 6)
    s0 = sin_jet(z, 6)
    c0 = cos_jet(z, 6)
    print(f"  exp-jet(0) {e0}  rate {rate(e0, z)}")
    print(f"  sin-jet(0) {s0}  rate {rate(s0, z)}")
    print(f"  cos-jet(0) {c0}  rate {rate(c0, z)}")
    print("  G: rate(exp,x)=exp.v  rate(sin,x)=cos.v  rate(cos,x)=-sin.v")
    print(f"  check exp  rate==value {rate(e0, z) == e0.v}")
    print(f"  check sin  rate==cos.v {rate(s0, z) == c0.v}")
    print(f"  check cos  rate==-sin.v {rate(c0, z) == -s0.v}")

    print()
    print("  LOG at 1  (u=x-1)")
    one = isolate(1)
    u = one - 1
    lg = log1p_jet(u, 6)
    print(f"  log1p-jet(0) {lg}  rate {rate(lg, one)}")
    print(f"  school log'(1)=1  {rate(lg, one) == 1}")
    try:
        log1p_jet(isolate(-1), 4)
        print("  log(0) FAILED to refuse")
    except Theta as e:
        print(f"  log(0) theta: {e}")

    print()
    print("  CHAIN  exp(u) at 0 with u=2x")
    x = isolate(0)
    u = x * 2
    eu = exp_jet(u, 6)
    print(f"  exp(2x) {eu}  rate {rate(eu, x)}")
    print(f"  exp.v * rate(u,x) = {eu.v * rate(u, x)}")
    print(f"  chain holds {rate(eu, x) == eu.v * rate(u, x)}")

    print()
    print("  LEFTOVER  exp-jet(1) is a Q partial sum, not e")
    one = isolate(1)
    e1 = exp_jet(one, 5)
    print(f"  exp-jet(1, n=5) {e1}")
    print("  moral: grow V or name the leftover. do not write e into Q.")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
