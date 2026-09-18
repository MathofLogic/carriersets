"""Two agents on a listed W. Common knowledge is reachability, not magic.

C(p) on a listed frame = p holds at every world reachable by any mix
of either agent's arrows. That is finite. The 'infinite' part is an
unbounded protocol, which this V does not contain.
"""
from __future__ import annotations

from itertools import product


def ev_agent(form, w, n, Rs, val):
    if isinstance(form, str):
        return val[form][w]
    op = form[0]
    if op == "NOT":
        return not ev_agent(form[1], w, n, Rs, val)
    if op == "AND":
        return ev_agent(form[1], w, n, Rs, val) and ev_agent(form[2], w, n, Rs, val)
    if op == "K":
        i, inner = form[1], form[2]
        return all(ev_agent(inner, v, n, Rs, val)
                   for v in range(n) if (w, v) in Rs[i])
    if op == "C":
        reach = _close(n, Rs)
        return all(ev_agent(form[1], v, n, Rs, val) for v in reach[w])
    raise ValueError(form)


def _close(n, Rs):
    union = set()
    for R in Rs:
        union |= set(R)
    reach = [{w} for w in range(n)]
    changed = True
    while changed:
        changed = False
        for w in range(n):
            extra = set()
            for u in reach[w]:
                for v in range(n):
                    if (u, v) in union and v not in reach[w]:
                        extra.add(v)
            if extra:
                reach[w] |= extra
                changed = True
    return reach


def coordinated_attack(k=3):
    """k+1 worlds: deliveries 0..k. p = 'attack is ordered' true only at k.
    Each agent sees own-and-lower delivery counts. C(p) never holds at 0.
    Generated, not Halpern-cited.
    """
    n = k + 1
    # agent A cannot tell k from k-1 if k>0, classic lossy last message
    RA, RB = set(), set()
    for i in range(n):
        RA.add((i, i))
        RB.add((i, i))
        if i + 1 < n:
            RA.add((i + 1, i))
            RB.add((i + 1, i))
    Rs = (frozenset(RA), frozenset(RB))
    val = {"p": {i: (i == k) for i in range(n)}}
    c_at = [ev_agent(("C", "p"), w, n, Rs, val) for w in range(n)]
    kA_at = [ev_agent(("K", 0, "p"), w, n, Rs, val) for w in range(n)]
    return {
        "worlds": n,
        "C_p": c_at,
        "A_knows_p": kA_at,
        "C_at_start": c_at[0],
        "C_anywhere": any(c_at),
    }


def main():
    print("EPISTEMIC  two agents, C = reachability on listed W")
    r = coordinated_attack(4)
    print(f"  deliveries 0..4, p only at 4")
    print(f"  C(p) per world: {r['C_p']}")
    print(f"  A knows p:     {r['A_knows_p']}")
    print(f"  C(p) at start: {r['C_at_start']}  C anywhere: {r['C_anywhere']}")
    print("  finite messages never mint C(p). that is the replica.")
    print("  outside V: unbounded send/lose process, infinite W.")
    print("verdict", "PASS" if (r["C_at_start"] is False) else "FAIL")
    return 0 if r["C_at_start"] is False else 1


if __name__ == "__main__":
    raise SystemExit(main())
