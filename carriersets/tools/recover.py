"""Throw a system at a listed V. Read the frame. Update the map.

    PYTHONPATH=carriersets:. python3 carriersets/tools/recover.py

Not a characteristica of the universe. A signature of a cut.
"""
from itertools import product


def signature(V, NOT, AND, OR, D):
    rows = {}
    rows["LNC_val"] = all(AND(a, NOT(a)) == V[0] for a in V)
    rows["LEM_val"] = all(OR(a, NOT(a)) == V[-1] for a in V)
    rows["LNC_des"] = all(AND(a, NOT(a)) not in D for a in V)
    rows["LEM_des"] = all(OR(a, NOT(a)) in D for a in V)
    rows["DN"] = all(NOT(NOT(a)) == a for a in V)
    rows["AND_assoc"] = all(
        AND(AND(a, b), c) == AND(a, AND(b, c)) for a, b, c in product(V, V, V)
    )
    rows["AND_comm"] = all(AND(a, b) == AND(b, a) for a, b in product(V, V))
    rows["MP"] = all(
        (b in D) for a, b in product(V, V)
        if a in D and OR(NOT(a), b) in D
    )
    closed = all(NOT(a) in V for a in V) and all(
        AND(a, b) in V and OR(a, b) in V for a, b in product(V, V)
    )
    rows["closed"] = closed
    return rows


def show(name, V, NOT, AND, OR, D):
    s = signature(V, NOT, AND, OR, D)
    bits = " ".join(("Y" if s[k] else "N") + ":" + k for k in s)
    print(f"  {name:<18} V={list(map(str,V))} D={list(map(str,D))}")
    print(f"    {bits}")
    return s


def main():
    print("RECOVER  law signature on a listed V")
    V2 = (0, 1)
    V3 = (0, 0.5, 1)
    show("CL2", V2, lambda a: 1 - a, min, max, {1})
    show("K3", V3, lambda a: 1 - a, min, max, {1})
    show("LP", V3, lambda a: 1 - a, min, max, {0.5, 1})
    show("L3", V3, lambda a: 1 - a,
         lambda a, b: max(0, a + b - 1),
         lambda a, b: min(1, a + b), {1})
    show("Godel", V3, lambda a: 1 if a == 0 else 0, min, max, {1})
    show("prod-AND", V3, lambda a: 1 - a,
         lambda a, b: a * b, max, {1})
    print("  prod-AND closed? 0.5*0.5=0.25 in V3?", 0.25 in V3)
    print("  update the map: product needs a bigger V or a different G (min).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
