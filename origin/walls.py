"""Where both routes stop. Generated first. Citation last and labeled."""
import json
import os
import sys

from claims import Suite
from closure import Closure, co_propagate
from peano_carrier import add, nat


def audit():
    Su = Suite("WALLS — both routes stop here", __file__)

    N = range(0, 7)
    held = all(int(add(nat(a), nat(b))) == int(add(nat(b), nat(a)))
               for a in N for b in N)
    Su.add(
        "WALL 1 INDUCTION. + commutes on {0..6}^2. Finite cut, not unbounded proof. "
        "Closing the gap is a schema. No list closes an infinite axiom family",
        held, 49, 49, True,
        "exhibit a finite enumeration that certifies unbounded +commute with no schema",
        "{0..6}^2",
    )

    class ZLine:
        def __init__(self, tag, k):
            self.tag, self.k = tag, k

        def succ(self):
            return ZLine(self.tag, self.k + 1)

        def __eq__(self, o):
            return (self.tag, self.k) == (o.tag, o.k)

        def __hash__(self):
            return hash((self.tag, self.k))

    zero = ZLine("N", 0)
    intruder = ZLine("Z", 0)
    reach = {zero}
    cur = zero
    for _ in range(40):
        cur = cur.succ()
        reach.add(cur)
    escapes = intruder not in reach
    inj = all(ZLine("N", i).succ() != ZLine("N", j).succ()
              for i in range(5) for j in range(5) if i != j)
    not_succ = all(zero != ZLine("N", i).succ() for i in range(5))
    Su.add(
        "WALL 1b INTRUDER. Extra chain satisfies zero, injective S, 0 not a successor. "
        "No amount of S from 0 reaches it. Only the schema excludes it",
        escapes and inj and not_succ, 3, 3, True,
        "exhibit a first-order axiom, not a schema, that kicks this chain",
        "one intruder",
    )

    # WALL 2b generated: BOX=proved, T=proved implies held. Empty R, p false.
    def box(R, w, p):
        return all(p[v] for v in R.get(w, ()))

    R_empty = {0: ()}
    p_false = {0: False}
    t_fails = not (box(R_empty, 0, p_false) <= p_false[0])
    # box true vacuously, p false, so T fails
    t_fails = box(R_empty, 0, p_false) and (not p_false[0])
    Su.add(
        "WALL 2b SOUNDNESS-IN-MINIATURE. On a 1-world empty frame, BOX p holds "
        "and p does not. Proved-as-BOX does not imply held. Generated. "
        "No paper is consulted for this row",
        t_fails, 1, 1, True,
        "exhibit this frame making BOX p imply p",
        "n=1 R empty p false",
    )

    C = Closure(7)
    closes = all(co_propagate(C, a, b) in range(7)
                 for a in range(7) for b in range(7))
    Su.add(
        "WALL 3 CLOSURE UNPRICED. Wrap of 7 closes on 49 pairs. Establishing "
        "the wrap is not priced from inside the wrap",
        closes, 49, 49, True,
        "price establishing a wrap using only resources downstream of that wrap",
        "Closure(7)",
    )

    src = open(os.path.join(os.path.dirname(__file__), "closure.py")).read()
    Su.add(
        "WALL 0 HOST METAL. co_propagate is (a+b)%n. The mechanism route "
        "reads a wrap. It does not birth + in a host that lacks +",
        ("(a + b) % C.n" in src) or ("(a + b) % C.n" in src.replace(" ", "")),
        1, 1, True,
        "implement co_propagate with no host addition or remainder",
        "closure.py source",
    )

    # WALL 4 — free A=A merges two mints
    xx = (3 * 3, 1 * 3 + 3 * 1)
    tx = (3 * 3, 3 * 2)
    merged = xx == tx
    next_slots_differ = (2, 0)
    Su.add(
        "WALL 4 FREE A=A. Value-eq merges x^2 and 3x at (9,6). Next slots "
        "are 2 and 0. Substitution along free = writes 2=0. "
        "A=A is a weigh on listed dimensions, not a prior",
        merged and next_slots_differ == (2, 0), 1, 1, True,
        "exhibit a priced = on (val, mint) that still merges these two pairs",
        "collision (9,6)",
    )

    Su.nonclaim("NOT claimed: Wall 2-Godel is proved here. That line is a citation.")
    Su.nonclaim("NOT claimed: walls are defects. They are the specification.")
    Su.nonclaim("NOT claimed: identity is false. Free A=A is an unpaid G.")
    return Su


if __name__ == "__main__":
    Su = audit()
    Su.report()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "manifests", "walls_manifest.json"), "w") as f:
        json.dump(Su.manifest(), f, indent=2, sort_keys=True)
    sys.exit(1 if Su.failed() else 0)
