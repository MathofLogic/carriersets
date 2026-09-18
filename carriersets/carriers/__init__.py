"""Catalog as data.

LIVE    = every claim that names a check. Default gate. Paid or the
          build fails.
RAW/--all = the museum rows too (citations, open problems).
"""
from . import (propositional, modal, manyvalued, settype, mathematical,
               cs, physics, evidence, interpretations, process)


def _checked(carriers):
    out = []
    for c in carriers:
        cc = dict(c)
        cc["forces"] = [x for x in c.get("forces", []) if x.get("check")]
        cc["breaks"] = [x for x in c.get("breaks", []) if x.get("check")]
        if cc["forces"] or cc["breaks"]:
            out.append(cc)
    return out


RAW_SECTIONS = [
    ("Propositional Logic", propositional.CARRIERS),
    ("Modal Logic", modal.CARRIERS),
    ("Many-Valued Logic", manyvalued.CARRIERS),
    ("Set Theory & Type Theory", settype.CARRIERS),
    ("Mathematical Carriers", mathematical.CARRIERS),
    ("Computer Science", cs.CARRIERS),
    ("Physics", physics.CARRIERS),
    ("Probability & Evidence", evidence.CARRIERS),
    ("Measurement Interpretations", interpretations.CARRIERS),
    ("Generated Atlas", process.GENERATED),
]

LIVE_SECTIONS = [(t, _checked(cs)) for t, cs in RAW_SECTIONS]
ARCHIVE_SECTIONS = RAW_SECTIONS
SECTIONS = LIVE_SECTIONS
ALL_SECTIONS = RAW_SECTIONS + [("Hypothesis postcards", process.HYPOTHESIS)]
ALL = [c for _, cs_ in SECTIONS for c in cs_]
ARCHIVE = [c for _, cs_ in RAW_SECTIONS for c in cs_]
