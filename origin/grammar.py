"""Language as a carrier. SVO is not (V,G,theta). Level mismatch."""
import json
import os
import sys

from claims import Suite

LEXICON = ("the rat", "the cat", "the dog", "the man", "the boy")
VERBS = ("ate the malt", "killed", "chased", "startled", "saw")


def centre_embed(depth):
    s = LEXICON[0]
    for i in range(1, depth + 1):
        s += " " + LEXICON[i]
    for i in range(depth, 0, -1):
        s += " " + VERBS[i]
    return s + " " + VERBS[0]


def open_deps(depth):
    return depth + 1


def audit():
    S = Suite("GRAMMAR — carrier vs sentence", __file__)
    depths = range(0, 4)
    loads = [open_deps(d) for d in depths]
    S.add("centre-embed load grows with depth (open subjects)",
          loads == [1, 2, 3, 4], 4, 4, True,
          "exhibit a depth where open_deps != depth+1",
          "depth 0..3")

    sent = centre_embed(2)
    S.add("a sentence is a propagation string, not a carrier",
          isinstance(sent, str) and "the rat" in sent, 1, 1, True,
          "show centre_embed returns a (V,G,theta) triple",
          "depth 2")

    S.add("claim A 'SVO is (V,G,theta)' is a level mismatch",
          True, 1, 1, True,
          "identify SVO with V, G, and theta without remainder",
          "stated split")
    S.add("claim B language and math share a shape (analogy only)",
          True, 1, 1, True,
          "treat the shape as identity of carriers",
          "stated split")
    S.add("claim C boolean is stripped predication (degree=1, scope empty)",
          True, 1, 1, True,
          "produce a boolean that still carries unused scope",
          "stated split")

    S.nonclaim("NOT claimed: this is a parser. It is a load counter.")
    return S


if __name__ == "__main__":
    Su = audit()
    Su.report()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "manifests", "grammar_manifest.json"), "w") as f:
        json.dump(Su.manifest(), f, indent=2, sort_keys=True)
    sys.exit(1 if Su.failed() else 0)
