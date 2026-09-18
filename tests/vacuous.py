"""Empty all() is True in Python. That is not a kept promise."""
from __future__ import annotations

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from pl import LeavesV, certify, isolate


def check(name, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    return ok


def main():
    bad = 0
    bad += not check("all([]) is True in the host", all([]) is True)
    bad += not check("empty BOX is that refund, not a law", all([]) is True)
    c = certify(lambda z: z * z, values=(), seeds=())
    bad += not check("empty certify grid is not ok", c.ok is False)
    bad += not check("empty grid gauge_ok False", c.gauge_ok is False)
    try:
        isolate(True)
        bad += not check("bool leaves V", False)
    except LeavesV:
        bad += not check("bool leaves V", True)
    try:
        isolate(float("nan"))
        bad += not check("nan float leaves V", False)
    except LeavesV as e:
        bad += not check("nan float leaves V", "NaN" in str(e))
    print("VACUOUS", "PASSED" if bad == 0 else f"FAILED {bad}")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
