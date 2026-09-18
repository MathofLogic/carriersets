"""Generate every force/break. Citation is not a check."""
from __future__ import annotations

from modal.engine import all_frames, equiv, gl_shape, preorder, refl, serial
from modal.systems import SYSTEMS, run_system


def counts(nmax=3):
    c = dict(all=0, refl=0, pre=0, equiv=0, ser=0, gl=0)
    for n, R in all_frames(nmax):
        c["all"] += 1
        if refl(n, R):
            c["refl"] += 1
        if preorder(n, R):
            c["pre"] += 1
        if equiv(n, R):
            c["equiv"] += 1
        if serial(n, R):
            c["ser"] += 1
        if gl_shape(n, R):
            c["gl"] += 1
    return c


def fmt_cex(cex):
    if cex is None:
        return "-"
    n, R, val, w = cex
    return f"n={n} w={w} R={sorted(R)} p={val.get('p')}"


def main():
    print("MODAL REPO  generate, do not cite")
    print()
    c = counts(3)
    print(f"  frames n=1..3: {c['all']}")
    print(f"  refl {c['refl']}  preorder {c['pre']}  equiv {c['equiv']}  "
          f"serial {c['ser']}  GL-shape {c['gl']}")
    print()
    passed = 0
    checks = 0
    for s in SYSTEMS:
        r = run_system(s, nmax=3)
        print(f"== {r['key']} ==")
        print(f"  V     {r['V']}")
        print(f"  G     {r['G']}")
        print(f"  theta {r['theta']}")
        print(f"  out   {r['outside']}")
        name, ok, cex = r["force"]
        checks += 1
        passed += int(ok)
        print(f"  FORCE {name:4}  {'PASS' if ok else 'FAIL'}  {fmt_cex(cex)}")
        if r["breaks"]:
            bname, died, bcex = r["breaks"]
            checks += 1
            passed += int(died)
            print(f"  BREAK {bname:4}  {'PASS' if died else 'FAIL'}  {fmt_cex(bcex)}")
        if "split" in r:
            sl = r["split"]
            checks += 2
            a, b = sl["two_loops_contingent"], sl["blob_contingent"]
            passed += int(a is False) + int(b is True)
            print(f"  SPLIT two-loops contingent={a}  blob contingent={b}")
        print()
    print(f"{passed}/{checks} generated checks passed")
    print("ALL PASS" if passed == checks else "SOME FAILED")
    return 0 if passed == checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
