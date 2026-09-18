# mathoflogic

A cut-and-ledger tool for formal systems.

You list three knobs:

```
V       what values may appear
G       what maps are allowed
theta   what happens when a write misses V
```

One operator:

```
P / G -> Q
```

Read P under G. Q is the result. A rate is two channels under one cut:

```
rate(P, G) = P.r / G.r
```

There is no independent variable with a life of its own. There is no
grounding slot. `=` is a scale (it costs a weigh). `A=A` is not free.

Nouns are labels. They compress a cut. They do not report entities.

This folder is a map of maps. It is not a floor under arithmetic,
Hayek, DNA, or Python.

---

## Test with one file (no repo)

Copy `pl/PROCESS.py` somewhere. Stdlib only (`fractions`).

```
python3 PROCESS.py
```

That self-check should print `verdict PASS`.

Then:

```
python3 -c "
from PROCESS import isolate, rate, certify, LeavesV
x = isolate(3)
print(rate(x*x, x))
print(certify(lambda z: z*z, at=3))
try:
    isolate(3.0)
except LeavesV as e:
    print(e)
"
```

You should see:

```
6
Certificate(... value='6' ... tier='FORCED-on-cut' ... gauge_ok=True)
float unlistable; use Fraction('3') or int
```

V is `int` or `Fraction`. `float`, `bool`, and NaN-shaped marks leave V.

That is the kernel. Everything else in the repo is a presentation of
the same loop.

---

## First course (six moves)

Side-by-side with Calc I lives here:

```
PYTHONPATH=process-calc:. python3 -m pcalc.lessons
PYTHONPATH=. python3 -m studio.steps
```

`lessons` prints the six moves: reading, rate, Leibniz mix, chain,
pole as theta, stop before a second slot.

`studio.steps` prints the tape: pair path 5 ops to 6; school path
5 ops to 6+h; deleting h is not + * / on Q.

Teacher notes, problem book, bridge sheet so they still sit the
other exam:

```
process-calc/docs/TEACHER.md
process-calc/docs/PROBLEMS.md
process-calc/docs/BRIDGE.md
process-calc/README.md
```

Labs: rate, units, fd, FTC, jet, history, **trans**, **vec**.
Same polynomial numbers as Calc I. Trig/exp/log: init + jet in Q,
leftover named. Vector: several isolators.

---

## Test with the repo

From this directory:

```
PYTHONPATH=. python3 -c "from pl import isolate, rate; x=isolate(3); print(rate(x*x, x))"
PYTHONPATH=. python3 tests/skeptic.py
PYTHONPATH=. python3 tests/vacuous.py
python3 verify.py
```

`verify.py` is the gate. It runs origin, modal, studio, mechanism,
logic census, skeptic, vacuous-pass hunt, and process-carrier checks.

Default library (generated rows only):

```
python3 carriersets/library_verify.py
```

Hypothesis postcards (DNA tape, language skits, econ miniatures) are
STIPULATED and not in that headline:

```
python3 carriersets/library_verify.py --all --section "Hypothesis postcards"
```

---

## What the folders are

```
pl/PROCESS.py     kernel. isolate, rate, certify, Runtime, ledger, mu
pl/__init__.py    from pl import isolate, rate, certify, Runtime
mechanism/        traveler seed. V G theta fall out if A=A is refused
origin/           two routes to a wrap. walls. composite CONDITIONAL
modal/            frames generated n<=3 (530). correspondence is a filter
process-calc/     labs. same Reading as PROCESS
studio/           steps, eq scale, substance-bug map, logic census, operators
docs/             ECON_MAP, PHYSARUM, SUBSTANCE_BUG (stipulated readings)
carriersets/      catalog + recover + library_verify
tests/            skeptic (headline numbers) and vacuous (empty-all)
docs/             maps, including ECON_MAP.md
```

Generated atlas (paid when the check searches a space): process pairs,
origin wrap, modus, modal frames, traveler, priced `=`, Z/n, S3,
operators-as-programs.

Hypothesis postcards (STIPULATED): DNA tape, Python `+`, Rust-shaped
move, Java-shaped unbox, budget, ledger, Goodhart, Hayek signal,
Lucas slope, ghost-close. Analogies. Not the same rung.

---

## How to read a claim

1. Name V, G, theta or it is not a claim yet.
2. Run a check that can fail if the generator moves.
3. If the write misses V, refuse or register a migration. Do not append.
4. If two presentations match, grow V before calling them identical.
5. Work goes on the ledger. Zero-cost work is an accounting failure.

Tiers: FORCED / EMPIRICAL / CONDITIONAL are paid.
STIPULATED / PRESUMED / OPEN / UNPAID are not.

Empty `all([])` is True in Python. That is the dead-world BOX refund.
It is a named wall, not a kept promise. `tests/vacuous.py` locks that
an empty certify grid is not `ok`.

---

## Falsifiers

`FALSIFIERS.md` and `tests/skeptic.py`.

If `rate(x*x,x)` at 3 is not 6, the first-command story is a lie.
If assoc on V3 labels is not 113, the census is a lie.
If frames n<=3 is not 530, the modal generator moved.

---

## Scope

Origin composite is CONDITIONAL: host `+` is Wall 0.
Mechanism does not describe stars.
Hypothesis rows do not instantiate Hayek, DNA-as-ontology, or Rustc.
`pip install` without PYTHONPATH is not the product yet. Copy PROCESS.py.

Replica, receipt, ledger line. Or it did not happen.
