# Re-audit of workbook (2) + workbook_verified.py

Ran `workbook_verified (1).py`: 22/22 ALL PASS.

Against WORKBOOK_ISSUES.md:

| # | was | now |
|---|---|---|
| 1 M5 vs Module 4 | ERROR | FIXED in stamps and CHECKS (`m4_*`). Comment in .py still says `MODULE 5`. |
| 2 garbled close names | SLIP | FIXED. Close list matches runner: lnc, lem, survives, m4_*. |
| 3 missing M1_CLOSURE_PROD / IMPLIES | GAP | FIXED. Both in CHECKS. |
| 4 triple NOT | ERROR | FIXED. Ask-yourself is NOT(NOT(v))=v. |
| 5 AND_min / AND_prod prose | SLIP | FIXED. |
| 6 Exercise 4.2 `-2=` | SLIP | FIXED. `y=(2x)^2=4x^2`. |
| 7 ten vs nine | SLIP | FIXED. "nine carriers." |
| 8 rate with no θ | GAP | FIXED. Guard + `M4_DEAD_ISOLATOR_REFUSES`. |
| 9 G is a coin | SLIP | FIXED. "G is insert_coin -- the move, not the coin." |
| 10 blank page 9 | SLIP | FIXED. Exercises 2.1–2.2 live there. |
| 11 min as the only repair | SCOPE | HALF. Prose now names Łuk AND/OR, LEM holds there. The Łuk box is stamped FORCED and has **no TEST: name** and **no line in CHECKS**. |
| 12 "Natural Form" | SCOPE | OPEN. Title unchanged. |
| 13 5-op tape | GAP | OPEN. Still claimed "checkable," still not a test. |
| 14 collision follow-up | SCOPE | FIXED. Grow to a jet or keep the function name. |
| 15 volume 2 list | SCOPE | Unchanged. Fine. |

---

## Still open

1. `.py` header: `# MODULE 5 -- Calculus in its natural form`  
   Module 4. Rename the comment.

2. Łuk chalkboard is FORCED without a runner line.  
   Contract on page 2: every stamp is a test in the file.  
   Add `m2_luk_closes` and `m2_luk_lem_holds`, or drop the FORCED stamp and mark STIPULATED/ANALOGY.

3. Title still says "natural form." Fights page 2 ("not the territory").

4. No ops tape. Five + * / to 6 vs five + * / to 6+h is still the missing chalkboard for the "checkable comparison" paragraph.

---

## Verdict

Better. The file and the book now agree on 22 named checks, including the two Module 1 tests and the dead isolator. Remaining work is the four rows above, not another pass over V2/V3/Z/n/gauge.
