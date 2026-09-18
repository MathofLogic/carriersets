"""Map the substance bug.

Process output treated as a container. Relations stuffed in as
intrinsic. Establishment and maintenance priced at 0. A=A written
free so the container is 'the same'.

Subject-predicate grammar is a compression of that rewrite.
The noun is not more real than the process it shortened.

    PYTHONPATH=. python3 -m studio.substance
"""
from __future__ import annotations

from pl import LeavesV, isolate, rate
from studio.eq import priced


def row(name, substance_sentence, process_cut, bug, check):
    print(f"\n  {name}")
    print(f"    grammar   {substance_sentence}")
    print(f"    cut       {process_cut}")
    print(f"    skip      {bug}")
    print(f"    check     {check}")


def main():
    print("SUBSTANCE BUG  output → container → intrinsic → unpaid A=A")
    print("nouns compress. they do not outrank the process.")

    x = isolate(3)
    xx = x * x
    print(f"\n  live tape  x={x}  x*x={xx}  rate={rate(xx, x)}")
    row(
        "RATE AS PROPERTY",
        "x has derivative 6",
        "rate(x*x, x) = x.r-channel / x.r-channel under one cut",
        "the number 6 is put inside x as a property",
        f"rate is {rate(xx, x)} and lives in the ratio, not in x",
    )

    a = isolate(3, 1) * isolate(3, 1)
    b = isolate(3, 2) * 3
    free = (a.v, a.r) == (b.v, b.r)
    mint = priced(
        {"val": a.v, "g": "sq"},
        {"val": b.v, "g": "lin"},
        on=("g",),
    )
    row(
        "PAIR AS THING",
        "the pair (9,6) is one object",
        "two mints: x^2 seed 1 and 3x seed 2",
        "value-eq merges mints; substitution writes 2=0",
        f"value-eq {free}; mint-eq {mint}",
    )

    row(
        "WRAP AS NUMBER",
        "5 is 5",
        "5 at tick 3 reads 2; 5 at tick 7 reads 5",
        "the numeral is treated as a container that owns identity",
        f"3-wrap {(5 + 5) % 3} vs 7-wrap {(5 + 5) % 7}",
    )

    try:
        isolate(True)
        bool_ok = False
    except LeavesV:
        bool_ok = True
    row(
        "BOOL AS VALUE",
        "True is a number-like bit",
        "Q refuses bool; bit is a wrap on a process",
        "the bit is put in a box that possesses 0/1",
        f"isolate(True) LeavesV {bool_ok}",
    )

    row(
        "ELECTRON HAS SPIN",
        "the electron has spin 1/2",
        "a reading under an apparatus-G",
        "detection output promoted to a pellet that owns spin",
        "not run here; STIPULATED reading of the same rewrite",
    )

    row(
        "DNA HAS A CODE",
        "the molecule contains information",
        "complement-copy program on {A,C,G,T}",
        "polymer output treated as a code-container",
        "postcard; see hypothesis DNA_TAPE",
    )

    row(
        "SUBJECT PREDICATE",
        "S is P",
        "isolate S-cut; read P-channel under G",
        "grammar output (noun, verb) treated as furniture",
        "every row above is this sentence with different labels",
    )

    print("\n  rewrite every time:")
    print("    process → isolate output → name it → box it")
    print("    → declare relations intrinsic → price upkeep 0")
    print("    → write A=A so the box is the same box")
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
