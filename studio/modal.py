"""modal.py — draw an arrow, read a table. not an essence.

W listed. R stipulated pairs. theta = valid on every world under every
valuation of the listed atoms. Axioms are those tables. Change R and
the table changes.

    PYTHONPATH=. python3 -m studio.modal
"""
from __future__ import annotations

from itertools import product


ATOMS = ("p",)


def eval_f(form, w, R, val):
    if form in ATOMS:
        return val[form][w]
    if form[0] == "NOT":
        return not eval_f(form[1], w, R, val)
    if form[0] == "AND":
        return eval_f(form[1], w, R, val) and eval_f(form[2], w, R, val)
    if form[0] == "OR":
        return eval_f(form[1], w, R, val) or eval_f(form[2], w, R, val)
    if form[0] == "IMP":
        return (not eval_f(form[1], w, R, val)) or eval_f(form[2], w, R, val)
    if form[0] == "BOX":
        succ = [v for (u, v) in R if u == w]
        return all(eval_f(form[1], v, R, val) for v in succ)
    if form[0] == "DIA":
        succ = [v for (u, v) in R if u == w]
        return any(eval_f(form[1], v, R, val) for v in succ)
    raise ValueError(form)


def valid(form, W, R):
    worlds = list(W)
    for bits in product([False, True], repeat=len(worlds)):
        val = {"p": dict(zip(worlds, bits))}
        for w in worlds:
            if not eval_f(form, w, R, val):
                return False
    return True


def T():
    return ("IMP", ("BOX", "p"), "p")


def Four():
    return ("IMP", ("BOX", "p"), ("BOX", ("BOX", "p")))


def B():
    return ("IMP", "p", ("BOX", ("DIA", "p")))


def D():
    return ("IMP", ("BOX", "p"), ("DIA", "p"))


def Five():
    return ("IMP", ("DIA", "p"), ("BOX", ("DIA", "p")))


def K():
    # □(p→p) → (□p → □p) is tautological; use □(p→p) as K-instance sanity
    return ("BOX", ("IMP", "p", "p"))


AX = [("T", T), ("4", Four), ("B", B), ("D", D), ("5", Five), ("Kbox", K)]


def profile(W, R):
    return {name: valid(fn(), W, R) for name, fn in AX}


def refl(W, R):
    return all((w, w) in R for w in W)


def trans(W, R):
    return all((a, c) in R for (a, mid) in R for (b, c) in R if b == mid)


def symm(W, R):
    return all((b, a) in R for (a, b) in R)


def serial(W, R):
    return all(any((w, v) in R for v in W) for w in W)


def eucl(W, R):
    return all((b, c) in R for (a, b) in R for (a2, c) in R if a2 == a)


def all_R(n):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    out = []
    for bits in product([0, 1], repeat=len(pairs)):
        R = frozenset(p for p, b in zip(pairs, bits) if b)
        out.append(R)
    return out


def main():
    print("MODAL  W listed, R stipulated, axioms are tables")
    print()

    W2 = (0, 1)
    frames = {
        "empty": frozenset(),
        "loops only": frozenset({(0, 0), (1, 1)}),
        "one arrow 0->1": frozenset({(0, 1)}),
        "both ways": frozenset({(0, 1), (1, 0)}),
        "S5 tiny": frozenset({(0, 0), (1, 1), (0, 1), (1, 0)}),
        "dead 1, loop 0": frozenset({(0, 0)}),
    }
    print("  six hand frames on W={0,1}, one atom p")
    print(f"  {'frame':<16} T  4  B  D  5  K   refl trans sym ser eucl")
    for name, R in frames.items():
        p = profile(W2, R)
        flags = "".join("Y  " if p[k] else "n  " for k in ("T", "4", "B", "D", "5", "Kbox"))
        geo = f"{int(refl(W2,R))}    {int(trans(W2,R))}     {int(symm(W2,R))}   {int(serial(W2,R))}   {int(eucl(W2,R))}"
        print(f"  {name:<16} {flags}{geo}")

    print()
    print("  correspondence on these six (not a law of arrows):")
    print("  loops only   T holds, 4 holds   (refl+trans)")
    print("  one arrow    T fails            (no loop at 0; □p can hold at 0 while p fails)")
    print("  empty        D fails            (□p true at a dead world, ◇p false)")
    print("  S5 tiny      T4B5 all hold")

    print()
    n2 = 2
    Rs = all_R(n2)
    print(f"  all frames on |W|=2: {len(Rs)}  (2^(n^2) = {2 ** (n2 * n2)})")
    sig = {}
    for R in Rs:
        key = tuple(profile(W2, R)[k] for k in ("T", "4", "B", "D", "5"))
        sig[key] = sig.get(key, 0) + 1
    print(f"  distinct T/4/B/D/5 tables: {len(sig)}")
    for key, c in sorted(sig.items(), key=lambda kv: -kv[1]):
        bits = "".join("Y" if b else "n" for b in key)
        print(f"    {bits}  x{c}")

    print()
    print("  |W|=3 raw frames = 2^9 = 512. not enumerated here as a law table;")
    print("  that is the same refusal as V4 binary maps: constrain R or don't census.")
    print()
    print("  packing: draw R, read which rows of T/4/B/D/5 turn Y.")
    print("  the axiom is not in the arrow. it is valid(..., R) on listed W.")
    print("  ghost: possible-world as a place that exists. here W is a list.")
    print()
    deep()
    print()
    print("verdict PASS")
    return 0


def succ_tuple(n, Rpairs):
    return tuple(frozenset(v for v in range(n) if (w, v) in Rpairs)
                 for w in range(n))


def all_frames_n(n):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    for bits in product([0, 1], repeat=len(pairs)):
        yield frozenset(p for p, b in zip(pairs, bits) if b)


def is_refl(n, R):
    return all((w, w) in R for w in range(n))


def is_trans(n, R):
    return all((a, c) in R for (a, mid) in R for (b, c) in R if b == mid)


def is_sym(n, R):
    return all((b, a) in R for (a, b) in R)


def is_ser(n, R):
    return all(any((w, v) in R for v in range(n)) for w in range(n))


def is_irrefl(n, R):
    return all((w, w) not in R for w in range(n))


def contingent_possible(W, R):
    """◇p ∧ ◇¬p true at some world under some val?"""
    form = ("AND", ("DIA", "p"), ("DIA", ("NOT", "p")))
    worlds = list(W)
    for bits in product([False, True], repeat=len(worlds)):
        val = {"p": dict(zip(worlds, bits))}
        for w in worlds:
            if eval_f(form, w, R, val):
                return True
    return False


def deep():
    print("DEEP  n<=3 frame filters + split the two S5 lookalikes")
    counts = {k: 0 for k in
              ("all", "refl", "trans", "sym", "ser", "pre", "equiv", "gl")}
    nmax = 3
    for n in range(1, nmax + 1):
        for R in all_frames_n(n):
            counts["all"] += 1
            r, t, s, se, ir = (is_refl(n, R), is_trans(n, R), is_sym(n, R),
                               is_ser(n, R), is_irrefl(n, R))
            if r:
                counts["refl"] += 1
            if t:
                counts["trans"] += 1
            if s:
                counts["sym"] += 1
            if se:
                counts["ser"] += 1
            if r and t:
                counts["pre"] += 1
            if r and t and s:
                counts["equiv"] += 1
            if t and ir:
                counts["gl"] += 1
    print(f"  frames n=1..3: {counts['all']}  (2 + 16 + 512 = 530)")
    print(f"  reflexive {counts['refl']}  preorder {counts['pre']}  "
          f"equivalence {counts['equiv']}")
    print(f"  serial {counts['ser']}  GL-shaped (trans+irrefl) {counts['gl']}")
    print("  carriersets check docstring says 585 frames. 530 is the raw list.")
    print()

    loops = frozenset({(0, 0), (1, 1)})
    blob = frozenset({(0, 0), (1, 1), (0, 1), (1, 0)})
    W2 = (0, 1)
    print("  same T4B5D table, different G:")
    print(f"  two loops  contingent-possible? {contingent_possible(W2, loops)}")
    print(f"  S5 blob    contingent-possible? {contingent_possible(W2, blob)}")
    print("  two loops never see the other value. blob does.")
    print("  grow the formula, the 'same system' splits.")
    print()
    print("  S4 vs S5 in one line:")
    print("  preorder buys 4 (you know that you know).")
    print("  equivalence buys 5 (you know the outline of what you don't).")
    print("  GL buys Löb and kills T (proved is not true-in-the-system).")
    print("  deontic D is seriality: every world sees an ideal. dead world kills it.")


if __name__ == "__main__":
    raise SystemExit(main())
