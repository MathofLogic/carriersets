"""Finite frames. Generate the table. Do not cite it."""
from __future__ import annotations

from itertools import product


def frames(n):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    for bits in product((0, 1), repeat=n * n):
        yield frozenset(p for p, b in zip(pairs, bits) if b)


def all_frames(nmax=3):
    for n in range(1, nmax + 1):
        for R in frames(n):
            yield n, R


def refl(n, R):
    return all((w, w) in R for w in range(n))


def trans(n, R):
    return all((a, c) in R for (a, mid) in R for (b, c) in R if b == mid)


def symm(n, R):
    return all((b, a) in R for (a, b) in R)


def serial(n, R):
    return all(any((w, v) in R for v in range(n)) for w in range(n))


def irrefl(n, R):
    return all((w, w) not in R for w in range(n))


def preorder(n, R):
    return refl(n, R) and trans(n, R)


def equiv(n, R):
    return preorder(n, R) and symm(n, R)


def gl_shape(n, R):
    return trans(n, R) and irrefl(n, R)


def ev(form, w, n, R, val):
    if isinstance(form, str):
        return val[form][w]
    op = form[0]
    if op == "NOT":
        return not ev(form[1], w, n, R, val)
    if op == "AND":
        return ev(form[1], w, n, R, val) and ev(form[2], w, n, R, val)
    if op == "OR":
        return ev(form[1], w, n, R, val) or ev(form[2], w, n, R, val)
    if op == "IMP":
        return (not ev(form[1], w, n, R, val)) or ev(form[2], w, n, R, val)
    if op == "BOX":
        return all(ev(form[1], v, n, R, val) for v in range(n) if (w, v) in R)
    if op == "DIA":
        return any(ev(form[1], v, n, R, val) for v in range(n) if (w, v) in R)
    raise ValueError(form)


def valuations(n, atoms=("p",)):
    k = len(atoms)
    for bits in product((False, True), repeat=n * k):
        val = {}
        for i, a in enumerate(atoms):
            val[a] = {w: bits[i * n + w] for w in range(n)}
        yield val


def forced(form, filt, nmax=3, atoms=("p",)):
    """True at every world of every passing frame under every val.
    On fail return (False, (n,R,val,w))."""
    for n, R in all_frames(nmax):
        if not filt(n, R):
            continue
        for val in valuations(n, atoms):
            for w in range(n):
                if not ev(form, w, n, R, val):
                    return False, (n, R, val, w)
    return True, None


def holds_somewhere(form, filt, nmax=3, atoms=("p",)):
    for n, R in all_frames(nmax):
        if not filt(n, R):
            continue
        for val in valuations(n, atoms):
            for w in range(n):
                if ev(form, w, n, R, val):
                    return True, (n, R, val, w)
    return False, None


T = ("IMP", ("BOX", "p"), "p")
FOUR = ("IMP", ("BOX", "p"), ("BOX", ("BOX", "p")))
FIVE = ("IMP", ("DIA", "p"), ("BOX", ("DIA", "p")))
B = ("IMP", "p", ("BOX", ("DIA", "p")))
D = ("IMP", ("BOX", "p"), ("DIA", "p"))
K = ("IMP", ("BOX", ("IMP", "p", "q")),
     ("IMP", ("BOX", "p"), ("BOX", "q")))
LOB = ("IMP", ("BOX", ("IMP", ("BOX", "p"), "p")), ("BOX", "p"))
DUAL = ("IMP", ("DIA", "p"), ("NOT", ("BOX", ("NOT", "p"))))
CONTINGENT = ("AND", ("DIA", "p"), ("DIA", ("NOT", "p")))
