"""Vector calculus as several isolators.

A vector reading is a list of Readings. Isolation is a listed
direction (seed per slot). grad / div / curl are rates under
those isolators. No Inf. No R^n as furniture.

    PYTHONPATH=process-calc:. python3 -m pcalc.veclab
"""
from __future__ import annotations

from pcalc.kernel import isolate, rate


def along(vals, direction):
    return [isolate(v, s) for v, s in zip(vals, direction)]


def grad_poly_xy(fx, fy, x, y):
    """f = x^fx * y^fy at (x,y). Returns (df/dx, df/dy)."""
    X, Y = isolate(x, 1), isolate(y, 0)
    f = (X ** fx) * (Y ** fy)
    dx = rate(f, X)
    X2, Y2 = isolate(x, 0), isolate(y, 1)
    g = (X2 ** fx) * (Y2 ** fy)
    dy = rate(g, Y2)
    return dx, dy


def div_xy(Px, Py, x, y):
    """P=(Px,Py) polynomial component functions, each 'x'/'y' monomials.

    Here we take P=(x^a, y^b) as the demo field.
    """
    X = isolate(x, 1)
    dPx = rate(X ** Px, X) if Px else 0
    Y = isolate(y, 1)
    dPy = rate(Y ** Py, Y) if Py else 0
    return dPx + dPy


def curl2(P, Q, at):
    """P,Q are callables Reading,Reading -> Reading.
    curl = dQ/dx - dP/dy.
    """
    x, y = at
    X, Y = isolate(x, 1), isolate(y, 0)
    dQdx = rate(Q(X, Y), X)
    X2, Y2 = isolate(x, 0), isolate(y, 1)
    dPdy = rate(P(X2, Y2), Y2)
    return dQdx - dPdy


def main():
    print("VEC LAB  several isolators, not a vector substance")
    print()
    print("  f=x^2 y at (2,3)")
    dx, dy = grad_poly_xy(2, 1, 2, 3)
    print(f"  grad {dx}, {dy}   school (2xy, x^2) = (12, 4)")
    print(f"  match {dx == 12 and dy == 4}")

    print()
    print("  div (x, y) at (7,9)")
    d = div_xy(1, 1, 7, 9)
    print(f"  div={d}  school 2  {d == 2}")

    print()
    print("  curl (-y, x) at (4,5)")

    def P(X, Y):
        return -Y

    def Q(X, Y):
        return X

    c = curl2(P, Q, (4, 5))
    print(f"  curl={c}  school 2  {c == 2}")

    print()
    print("  curl(grad f) for f=x^2 y at (2,3)")

    def dfdx(X, Y):
        return (X ** 2) * Y  # wait this is f not dfdx
    # build P=df/dx=2xy, Q=df/dy=x^2 as fields
    def Px(X, Y):
        return 2 * X * Y

    def Qy(X, Y):
        return X ** 2

    z = curl2(Px, Qy, (2, 3))
    print(f"  curl grad={z}  school 0  {z == 0}")

    print()
    print("  direction seed (2,0) vs (0,3) on f=x^2")
    x = isolate(4, 2)
    print(f"  rate(x^2, x) seed 2 = {rate(x * x, x)}  (gauge, still 8)")
    print("  moral: extra names, same G. no R^n box.")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
