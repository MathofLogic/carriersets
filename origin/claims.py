"""Claim ledger. Tier is computed. No metaphysics slot."""
from __future__ import annotations


ORDER = ("UNPAID", "CONDITIONAL", "FORCED-on-cut", "FORCED")


def tier(n, scope, declared, derived):
    if derived and (n == 0 or scope is None):
        return "CONDITIONAL"
    if declared and scope is not None and n == scope and n > 0:
        return "FORCED-on-cut"
    if declared and scope is None and n > 0:
        return "FORCED"
    return "CONDITIONAL"


class Claim:
    def __init__(self, text, held, n, scope, declared, falsifier,
                 cut="", derived=False):
        if not falsifier:
            raise ValueError("no claim without a falsifier")
        self.text = text
        self.held = bool(held)
        self.n = int(n)
        self.scope = scope
        self.declared = bool(declared)
        self.derived = bool(derived)
        self.falsifier = falsifier
        self.cut = cut
        self.tier = "UNPAID" if not self.held else tier(
            self.n, self.scope, self.declared, self.derived)


class Suite:
    def __init__(self, title, source=""):
        self.title = title
        self.source = source
        self.claims = []
        self.notes = []

    def add(self, text, held, n, scope, declared, falsifier,
            cut="", derived=False):
        self.claims.append(Claim(
            text, held, n, scope, declared, falsifier, cut, derived))

    def nonclaim(self, text):
        self.notes.append(text)

    def failed(self):
        return [c for c in self.claims if not c.held]

    def verdict(self):
        if self.failed():
            return "UNPAID"
        ranks = [ORDER.index(c.tier) for c in self.claims]
        return ORDER[min(ranks)] if ranks else "CONDITIONAL"

    def manifest(self):
        return {
            "title": self.title,
            "verdict": self.verdict(),
            "claims": [
                {
                    "text": c.text,
                    "held": c.held,
                    "n": c.n,
                    "scope": c.scope,
                    "tier": c.tier,
                    "falsifier": c.falsifier,
                    "cut": c.cut,
                }
                for c in self.claims
            ],
            "notes": list(self.notes),
        }

    def report(self):
        print(self.title)
        print(f"  verdict {self.verdict()}  claims {len(self.claims)}")
        for c in self.claims:
            flag = "HOLD" if c.held else "FAIL"
            print(f"  [{c.tier:<14}] {flag}  n={c.n}  {c.text[:72]}")
        for n in self.notes:
            print(f"  {n}")
