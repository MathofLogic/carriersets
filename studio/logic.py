"""Logic workshop. Numbers computed on this run, not remembered."""
from itertools import product


def tables(V, fn):
    return tuple(fn(a, b) for a, b in product(V, V))


def assoc(V, fn):
    return all(fn(fn(a, b), c) == fn(a, fn(b, c)) for a, b, c in product(V, V, V))


def report():
    V2 = (0, 1)
    V3 = (0, 1, 2)

    def and_min(a, b):
        return min(a, b)

    def and_prod_v2(a, b):
        return a * b

    nbin_v2 = 2 ** (2 * 2)
    nbin_v3 = 3 ** (3 * 3)
    print("LOGIC  computed on this run")
    print(f"  |Bin(V2)|={nbin_v2}")
    print(f"  |Bin(V3)|={nbin_v3}")
    same = tables(V2, and_min) == tables(V2, and_prod_v2)
    print(f"  V2 min-AND == V2 prod-AND as tables: {same}")
    mid_prod = (1 / 2) * (1 / 2)
    print(f"  1/2 * 1/2 = {mid_prod}  in {{0,1/2,1}}? {mid_prod in (0, 0.5, 1)}")

    assoc_n = 0
    and_like = 0
    for cells in product(V3, repeat=9):
        def fn(a, b, cells=cells):
            return cells[a * 3 + b]
        if assoc(V3, fn):
            assoc_n += 1
            if fn(1, 1) == 1 and fn(0, 1) == 0 and fn(1, 0) == 0 and fn(0, 0) == 0:
                and_like += 1
    print(f"  Assoc on V3 labels={assoc_n}")
    print(f"  AND-like (1 absorb, 0 annihilate) among assoc={and_like}")
    print("  V4 |Bin|=4**16 is unlistable here. Constrain G.")
    return 0


def main():
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
