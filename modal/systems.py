"""Each row is a cut: V, G, theta. Outside V and breaks are generated."""
from __future__ import annotations

from modal.engine import (
    B, CONTINGENT, D, FIVE, FOUR, K, LOB, T,
    equiv, forced, gl_shape, holds_somewhere, preorder, refl, serial,
)


def any_frame(n, R):
    return True


SYSTEMS = [
    dict(
        key="K",
        V="listed W, listed R, atoms p (q for K)",
        G="BOX=all successors, DIA=any successor, R free",
        theta="valid = true at every world of every frame under every val",
        filt=any_frame,
        force=("K", K, ("p", "q")),
        break_=("T", T, ("p",)),
        outside="infinite W, unlistable R, common knowledge as unbounded protocol",
    ),
    dict(
        key="T",
        V="K plus every world has a loop",
        G="K + reflexivity",
        theta="self-access",
        filt=refl,
        force=("T", T, ("p",)),
        break_=("4", FOUR, ("p",)),
        outside="a world that cannot see itself (that frame left V)",
    ),
    dict(
        key="S4",
        V="preorder frames (refl+trans)",
        G="T + compose arrows",
        theta="reachable-from-reachable is already reachable",
        filt=preorder,
        force=("4", FOUR, ("p",)),
        break_=("5", FIVE, ("p",)),
        outside="sealed cells (symmetry). S4 knows that it knows, not what it does not",
    ),
    dict(
        key="S5",
        V="equivalence frames",
        G="S4 + reverse arrows",
        theta="worlds in a class are interchangeable",
        filt=equiv,
        force=("5", FIVE, ("p",)),
        break_=None,
        extra="contingent",
        outside="cross-class talk; a knower who cannot see a blind world",
    ),
    dict(
        key="D",
        V="serial frames (no dead world)",
        G="K + every world has a successor",
        theta="there is always an ideal / a next",
        filt=serial,
        force=("D", D, ("p",)),
        break_=None,
        outside="dead world: BOX true vacuously, DIA false. O->P dies there",
    ),
    dict(
        key="GL",
        V="transitive irreflexive frames (finite => well-founded)",
        G="BOX as proved-in-this-system",
        theta="proof depth ends",
        filt=gl_shape,
        force=("Löb", LOB, ("p",)),
        break_=("T", T, ("p",)),
        outside="T: proved does not imply true-in-the-system. arithmetic completeness of GL for PA is not this V",
    ),
]


def run_system(s, nmax=3):
    out = {"key": s["key"], "V": s["V"], "G": s["G"], "theta": s["theta"],
           "outside": s["outside"]}
    name, form, atoms = s["force"]
    ok, cex = forced(form, s["filt"], nmax=nmax, atoms=atoms)
    out["force"] = (name, ok, cex)
    if s["break_"]:
        bname, bform, batoms = s["break_"]
        bok, bcex = forced(bform, s["filt"], nmax=nmax, atoms=batoms)
        out["breaks"] = (bname, (not bok), bcex)
    else:
        out["breaks"] = None
    if s.get("extra") == "contingent":
        # two S5-shaped frames on n=2 already split this
        from modal.engine import frames
        loops = frozenset({(0, 0), (1, 1)})
        blob = frozenset({(0, 0), (1, 1), (0, 1), (1, 0)})
        out["split"] = {
            "two_loops_contingent": holds_somewhere(
                CONTINGENT, lambda n, R: n == 2 and R == loops, nmax=2)[0],
            "blob_contingent": holds_somewhere(
                CONTINGENT, lambda n, R: n == 2 and R == blob, nmax=2)[0],
        }
    return out
