# modal

Draw an arrow. Read a table. The table is generated.

```
PYTHONPATH=. python3 -m modal.verify
PYTHONPATH=. python3 -m modal.epistemic
```

22 lines of force/break come out of `modal.verify` as PASS/FAIL plus a
witness `(n, R, val, w)` when something breaks. No paper is consulted
for those rows.

Nouns (`world`, `necessity`, `knowledge`) compress a cut. They do not
report places.

---

## The cut

```
V     listed W, listed R, listed atoms
G     BOX = all successors, DIA = any successor
theta valid = true at every world of every frame in the filter,
      under every valuation of the atoms
```

Change the filter on R. A different axiom row turns Y.
That is the whole packing: "draw an arrow, get an axiom."

Outside this V: infinite W, unlistable R, a protocol with no bound,
arithmetic completeness of GL for PA.

---

## Generated census (n = 1..3)

```
frames      530     2 + 16 + 512
reflexive    69
preorder     34     S4-shaped
equivalence   8     S5-shaped   (Bell: 1+2+5)
serial      353     deontic D-shaped
GL-shape     23     trans + irrefl
```

`2^{n^2}` summed. Not 585. 585 was a leftover string in an older check.

---

## Systems

Each row is a filter on the same 530. Force and break are rerun, not stored.

| key | filter | force | break (witness printed) |
|---|---|---|---|
| K | all 530 | K | T at n=1, R empty, p false |
| T | 69 loops | T | 4 at a 3-world reflexive non-transitive frame |
| S4 | 34 preorders | 4 | 5 at n=2, R={(0,0),(1,0),(1,1)}, p true only at 1 |
| S5 | 8 equivalences | 5 | two-loops vs blob split on `◇p ∧ ◇¬p` |
| D | 353 serial | D / O→P | dead world is outside this V |
| GL | 23 | Löb | T at n=1, R empty, p false |

S4: you know that you know. You do not know the outline of what you
do not know.

S5: seal the cell (symmetry). Possibility becomes stable. That is
"absolute knowledge of what you don't know." It is θ, not a knower.

GL: BOX reads as proved-in-this-system. Löb holds on the 23. T does
not. Proved is not true-in-the-system. PA-completeness is another V.

D: no dead world. BOX at a dead world is `all([])=True`. DIA is false.
O→P dies there. Same refund button as the vending machine.

---

## Epistemic replica

`python -m modal.epistemic`

Two agents. C(p) = p at every world reachable by any mix of either
arrow. On a listed W that is finite.

Coordinated attack, k=4 deliveries, p only at world 4:

```
C(p) per world: [False, False, False, False, False]
C at start: False
```

Finite messages never mint C(p). The unbounded send/lose process is
not in this V. That sentence is the replica. It is not a citation of
Halpern and Moses.

---

## Why these are not ontological models

- W is a list of integers.
- R is a stipulated set of pairs.
- BOX is `all` over a successor list.
- A dead world makes BOX true because the list is empty, not because
  a necessity lives there.
- Two frames can share the T4B5 postcard and split when the formula
  grows (`◇p ∧ ◇¬p`).
- Adding symmetry does not discover ignorance. It removes the frames
  where ignorance has a shape you cannot see.

If a page says "possible worlds exist" or "S5 is the logic of
knowledge," that page left the cut. Put it down.

---

## Falsifiers

- A filter that forces T on a frame with a missing loop.
- A preorder that forces 5.
- `◇p ∧ ◇¬p` true at a world of the two-loop frame.
- C(p) true at world 0 of the k=4 attack replica.
- Löb false on one of the 23 GL-shaped frames with n<=3.

If any of those fire, the runner prints FAIL and the witness.
