"""Seed mechanism. V G theta fall out. A=A is not the start."""
from mechanism.cascade import run, vent_split
from mechanism.traveler import Traveler, time_to, until_theta
from mechanism.tropical import brute_monotone, min_plus


def main():
    print("MECHANISM  traveler / cascade / tropical")
    t0, t2, t8 = time_to(0), time_to(2), time_to(8)
    print(f"  arrivals L=0,2,8 -> {t0},{t2},{t8}")
    assert t0 < t2 < t8 and (t0, t2, t8) == (50, 150, 450)

    a, b = Traveler(eta=0.1, tag="a"), Traveler(eta=0.5, tag="b")
    for _ in range(20):
        a.step(1.0)
        b.step(1.0)
    print(f"  two seeds after 20: a=({a.x:.2f},{a.L:.2f}) b=({b.x:.2f},{b.L:.2f})")
    assert a.x != b.x and a.L != b.L

    tick, tr = until_theta(0.5, 12.0)
    print(f"  eta=0.5 theta=12 exceed tick {tick} L={tr.L:.2f}")
    assert tick == 167

    kept, kids = vent_split(12.0, 0.4)
    assert abs(kept + sum(kids) - 12) < 1e-12
    print(f"  vent kappa=0.4 conserved {kept + sum(kids)}")
    kept10, kids10 = vent_split(12.0, 0.1)
    v_core = 1 / (1 + kept10)
    v_kid = 1 / (1 + kids10[0])
    print(f"  kappa=0.1 child_faster? {v_kid > v_core}  (clause 4 is kappa-relative)")

    st = run(2.0, 3.0, 0.5)
    cy = run(2.0, 0.5, 0.85)
    co = run(2.0, 0.5, 0.02)
    print(f"  fates {st['regime']} {cy['regime']} {co['regime']}")
    assert st["regime"] == "STEADY"
    assert cy["regime"] == "CYCLIC"
    assert co["regime"] == "COLLAPSED"
    assert st["ledger"] < 1e-9 and cy["ledger"] < 1e-9

    grid = [[1, 4, 2], [3, 1, 5], [2, 2, 1]]
    bf, tp = brute_monotone(grid), min_plus(grid)
    print(f"  tropical 3x3 brute={bf} minplus={tp}")
    assert bf == tp

    print("  V = reachable (x,L). G = step/vent/min-plus. theta = split cap.")
    print("  = is a weigh after a tick. start-eq of two etas is unpaid.")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
