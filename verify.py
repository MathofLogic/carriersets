#!/usr/bin/env python3
"""Top gate. Each suite generates its own rows."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def run(title, args, cwd, env=None):
    print("=" * 70)
    print(title)
    print("=" * 70)
    e = os.environ.copy()
    if env:
        e.update(env)
    p = subprocess.run(args, cwd=cwd, env=e)
    return p.returncode == 0


def main():
    ok = True
    ok &= run("ORIGIN", [sys.executable, "tests/run.py"],
              os.path.join(ROOT, "origin"))
    ok &= run("MODAL", [sys.executable, "-m", "modal.verify"],
              ROOT, {"PYTHONPATH": ROOT})
    ok &= run("EPISTEMIC", [sys.executable, "-m", "modal.epistemic"],
              ROOT, {"PYTHONPATH": ROOT})
    ok &= run("STUDIO STEPS", [sys.executable, "-m", "studio.steps"],
              ROOT, {"PYTHONPATH": ROOT})
    ok &= run("EQ SCALE", [sys.executable, "-m", "studio.eq"],
              ROOT, {"PYTHONPATH": ROOT})
    ok &= run("MECHANISM", [sys.executable, "-m", "mechanism.verify"],
              ROOT, {"PYTHONPATH": ROOT})
    ok &= run("LOGIC CENSUS", [sys.executable, "-m", "studio.logic"],
              ROOT, {"PYTHONPATH": ROOT})
    ok &= run("SKEPTIC", [sys.executable, "tests/skeptic.py"], ROOT,
              {"PYTHONPATH": ROOT})
    ok &= run("VACUOUS", [sys.executable, "tests/vacuous.py"], ROOT,
              {"PYTHONPATH": ROOT})
    ok &= run("ATLAS CHECKS", [sys.executable, "-c",
              "import carrierlib.checks; "
              "from carrierlib.core import run_claim; "
              "from carriers.process import GENERATED as CARRIERS; "
              "bad=0\n"
              "for c in CARRIERS:\n"
              "  for k in ('forces','breaks'):\n"
              "    for cl in c[k]:\n"
              "      r=run_claim(cl)\n"
              "      print(r['check'], r['ok'], r['evidence'][:60])\n"
              "      bad += int(r['ok'] is False)\n"
              "raise SystemExit(bad)"],
              os.path.join(ROOT, "carriersets"),
              {"PYTHONPATH": os.path.join(ROOT, "carriersets")})
    print("=" * 70)
    print("MEGA GATE", "PASSED" if ok else "FAILED")
    print("=" * 70)
    print("NOT claimed: the atlas is the territory.")
    print("There is no grounding slot. Paid, unpaid, cited.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
