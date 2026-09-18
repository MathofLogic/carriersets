# Workbook issues and corrections

Source: *Formal Systems Engineering* workbook PDF (15 pages),
read 2026-09-17. Companion named `workbook_verified.py` was not in
the PDF folder here, so the printed 19-line transcript is treated
as the book's own grade sheet.

Status key:

- ERROR: contradicts the book's own arithmetic or labels
- SLIP: typo / numbering / layout
- GAP: claim the page cites but the grade sheet does not run
- SCOPE: honest limit the next pass should name

Nouns below are labels.

---

## 1. Module number vs test prefix

**SLIP.** Body Module 4 (calculus) stamps tests `M5_GAUGE_INVARIANT`,
`M5_COLLISION`, `M5_CHAIN_CANCELS`. Closing transcript uses `m5_*`
for the same three.

There is no Module 5 in this volume.

**Correction.** Rename to `M4_GAUGE_INVARIANT`, `M4_COLLISION`,
`M4_CHAIN_CANCELS` in the chalkboard, the companion file, and the
closing transcript. Keep one integer per module.

---

## 2. Grade sheet names do not match chalkboard names

**SLIP / GAP.** Closing chapter prints 19 identifiers. Several are
not the names stamped in Modules 1–2.

| printed | chalkboard stamp | correction |
|---|---|---|
| `m1_trnc` | `M1_LNC` | `m1_lnc` |
| `m1Item` | `M1_LEM` | `m1_lem` |
| `m2_trnc_fails` | `M2_LNC` | `m2_lnc_fails` |
| `m2Item_fails` | `M2_LEM` | `m2_lem_fails` |
| `m2_dn_survivies` | `M2_DN` | `m2_dn_survives` |
| `m5CollisionExact` | `M5_COLLISION` | `m4_collision` after (1) |

**Correction.** One string per test, identical in stamp, filename,
and closing printout.

---

## 3. Tests the body cites that the 19-line sheet omits

**GAP.** Module 1 stamps and describes:

- `M1_CLOSURE_PROD` (AND_prod closes on V2)
- `M1_IMPLIES` (implication table)

Neither appears in the closing 19.

Module 1 also walks LNC and LEM. Those are in the 19 under the
garbled names in (2). Double negation on V2 is asked in the
"before reading on" box, then tested as `M2_DN` on both carriers.
A separate `m1_dn` in the 19 is either a duplicate of the V2 half
of `M2_DN` or an unstamped extra.

**Correction.** Either add `m1_closure_prod` and `m1_implies` to
the runner and print 21/21, or remove those stamps from Module 1
so the contract stays "every stamp is a line in the final chapter."
Do not keep both stories.

---

## 4. Triple negation written where double negation is meant

**ERROR.** Module 1 "Ask yourself":

> does ¬¬¬(v) = v hold for every v in {0,1}?

Three NOTs. On V2:

```
NOT(NOT(NOT(0))) = NOT(NOT(1)) = NOT(0) = 1 ≠ 0
```

So ¬¬¬(v)=v is false. The law the book means, and that Module 2
rechecks, is ¬¬(v)=v.

**Correction.** Print `NOT(NOT(v)) = v`. Keep the "write both
cases by hand" instruction.

---

## 5. Garbled "does not cover" line in Module 1

**SLIP.** End of Module 1:

> Whether ¬¬¬ min and ¬¬¬ prod are really the same operation

**Correction.** `AND_min` and `AND_prod`.

---

## 6. Exercise 4.2 answer string

**SLIP.** Printed:

> Direct check: y=(2x)²-2=4x^2

The `-2=` is junk. At x=1, y=(2x)²=4x²=4, rate=8.

**Correction.** `y=(2x)²=4x²`. At x=1, y=4, rate(y,x)=8.

The rest of 4.2 is right: u=(2,2), y=(4,8), 4·2=8.

---

## 7. "Ten carriers" for n = 2..10

**SLIP.** Module 3: "the code above checked all ten by brute
enumeration." The table is n=2,3,4,5,6,7,8,9,10. That is 9 rows.

**Correction.** Say "nine carriers, n=2 through n=10." If n=1 was
run off-page, print the row.

Field column as printed (True on 2,3,5,7; False on 4,6,8,9,10)
matches Z/n being a field iff n is prime, on that list.

---

## 8. Displayed `rate` has no θ

**GAP.** Module 4 chalkboard:

```
def rate(top, bottom):
    return top.r / bottom.r
```

No check that `bottom.r != 0`. Module 0 taught refuse-or-grow.
A dead isolator is the refund button for this carrier.

**Correction.**

```
def rate(top, bottom):
    if bottom.r == 0:
        raise Theta("dead isolator")
    return top.r / bottom.r
```

Add `M4_DEAD_ISOLATOR` to the runner: `rate(Pattern(3,1), Pattern(3,0))`
refuses. That is one more FORCED line.

---

## 9. Two stories about what G is in Module 0

**SLIP.** How To Read: "In Module 0, G is a coin."
Module 0 body: G is `insert_coin`.

Those are different slots. Coin is a value in V. Insert is the map.

**Correction.** How To Read should say: V is the coin list,
G is insert (and later refund), θ is "total ≥ 35" plus refuse
foreign metal. Isolation in Module 0 is "read the total against
the machine's rules," not "G is a coin."

---

## 10. Page 9 is a stranded sentence

**SLIP.** Page 9 contains only the tail of Module 2's "does not
cover" box. Looks like a page-break dump.

**Correction.** Glue it to the end of Module 2 on page 8. Do not
ship a nearly blank leaf.

---

## 11. Min presented as "the" repair on V3

**SCOPE.** Module 2: product leaks, swap to min, name K3. True.

Other maps also close on {0, 1/2, 1}. Łukasiewicz AND
`max(0, a+b-1)` closes. On that G, LEM holds and AND-idempotent
fails. Min/max K3 is one repair, not the only closed G.

**Correction.** One sentence: "min is a repair that closes. It is
not the only closed AND on this V. Łukasiewicz AND also closes
and forces a different law table." Leave the full census to a
later module (we counted 113 associative binary maps on V3).
Do not imply K3 is forced by adding 1/2.

---

## 12. Calculus title "In Its Natural Form"

**SCOPE.** Conflicts with How To Read ("this book is not the
territory"). "Natural" reads as terrain.

**Correction.** Title options that stay maps:
"Calculus as rate of two channels" or "Module 4: pairs."

---

## 13. Op-count comparison is stated, not taped

**GAP.** Module 4 says the limit path adds an abstraction before
the first multiply, and calls that checkable. The volume never
prints the tape.

On this studio's runner (`python -m studio.steps`):

```
pair rate     ops=5  value=6
school / fd   ops=5  value=13/2
```

Same five + * / on Q. Pair output is 6. School output is 6+h.
Deleting h is not an op on Q.

**Correction.** Add chalkboard `M4_OPS_TO_SIX` that prints the
five pair ops and asserts value==6, and the five school ops and
asserts value==6+h. Falsifier: a finite + * / list on Q that
sends (f(3+h)-f(3))/h to 6 for generic h.

---

## 14. Collision is FORCED, then under-used

**SCOPE.** `(9,6)` is x² seed 1 and 3x seed 2. Correct.

The page does not say what to do next: a pair does not name the
situation. Isolation is the rest of the story. A 2-jet is a
bigger V if you need a second channel.

**Correction.** One line after the collision box: "To tell those
situations apart, grow V (jet) or keep the function name on the
ticket. Do not treat (v,r) as a complete object."

---

## 15. Next-volume list vs this studio

The close lists: rate budget, forced reification under a tight
ledger, FTC as telescope, Module 0 machine with math loaded.

This studio already has labs for FTC leftover, fd leftover,
units, and a ledger μ. They are not in the PDF. That is a
volume boundary, not an error.

**Correction.** If volume 2 ships, point each of those four at a
named test the same way volume 1 does. Do not leave "real,
tested, separate phenomenon" without a file.

---

## 16. What is already right (do not "fix")

Keep these. They match the arithmetic.

- V2 min table equals V2 product table (4 rows).
- V3 product leaks at (1/2, 1/2) -> 1/4.
- V3 min closes. LNC and LEM fail at 1/2 under min/max/NOT.
- DN holds on both carriers while NOT=1-v.
- Liar empty on V2, {1/2} on V3.
- Naturals leak under subtraction at 0-1.
- Z/n field on {2,3,5,7} only, in the printed range.
- 2*3=1 in Z/5. No inverse of 2 in Z/4.
- x²+1 roots {2,3} in Z/5, empty in Z/3.
- Gauge: seeds 1, 2, 1/2, 10, 1/3 all give rate 6 for x² at 3.
- Chain at x=2, u=x+1, y=u²: 6 = 6*1.
- Exercise 4.1: x³ at 2 is (8,12), rate 12.
- Two honest fixes only: refuse, or grow V out loud.
- FORCED means "on the carrier as stated," and the close says so.

---

## Patch order

1. Rename M5 -> M4. Fix transcript typos (2).
2. Either ship or drop `M1_CLOSURE_PROD` and `M1_IMPLIES` (3).
3. Fix ¬¬¬ and AND_min/prod prose (4, 5).
4. Fix Exercise 4.2 string (6).
5. "nine carriers" (7).
6. θ on `rate` plus one refuse test (8).
7. How To Read: G is insert, not "a coin" (9).
8. Kill blank page 9 (10).
9. Name Łuk as another closed AND (11).
10. Drop "natural form" (12).
11. Add the 5-op tape (13).
12. One sentence after collision (14).

After that, the 19-line (or 21-line) close and the chalkboard
stamps are the same list, and every number on the page is a
line the reader can run.
