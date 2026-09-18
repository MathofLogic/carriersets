"""Number theory as readings of a wrap. Integers are refuse-to-close."""
import json
import os
import sys

from claims import Suite
from closure import Closure, annihilates


def school_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def no_annihilator(n):
    C = Closure(n)
    return not any(annihilates(C, a, b)
                   for a in range(1, n) for b in range(1, n))


def audit():
    S = Suite("NUMBERS — from wrap", __file__)
    W, NS = 5, (3, 7, 12)
    readings = {n: W % n for n in NS}
    S.add("value is wrap-relative: 5 reads differently at 3, 7, 12",
          len(set(readings.values())) > 1, len(NS), len(NS), True,
          "exhibit a winding whose reading is identical at every wrap",
          f"winding {W} at {NS}")

    cut = range(2, 31)
    agree = all(no_annihilator(n) == school_prime(n) for n in cut)
    S.add("prime-on-wrap (no annihilating pair) agrees with school prime",
          agree, len(cut), len(cut), True,
          "exhibit n in 2..30 where the two predicates split",
          "n=2..30")

    fieldish = [n for n in range(2, 12)
                if all(any((a * b) % n == 1 for b in range(1, n))
                       for a in range(1, n))]
    S.add("wraps where every nonzero winding undoes under iterate are primes",
          fieldish == [2, 3, 5, 7, 11], len(range(2, 12)), len(range(2, 12)),
          True,
          "exhibit a composite n<12 where every nonzero has an iterate-inverse",
          "n=2..11")

    S.nonclaim("NOT claimed: priority on Lagrange or Fermat. Agreement is a check.")
    S.nonclaim("NOT claimed: Z is constructed. Z is refuse-to-close, unpaid past any n.")
    return S


if __name__ == "__main__":
    Su = audit()
    Su.report()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "manifests", "arithmetic_manifest.json"), "w") as f:
        json.dump(Su.manifest(), f, indent=2, sort_keys=True)
    sys.exit(1 if Su.failed() else 0)
