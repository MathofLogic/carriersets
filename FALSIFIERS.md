# Falsifiers

A claim here is only as good as the line that would kill it.
Run `PYTHONPATH=. python3 tests/skeptic.py`.

| claim | command | dies if |
|---|---|---|
| rate(x²,x) at 3 is 6 | `from pl import isolate, rate; rate(isolate(3)*isolate(3), isolate(3))` | result ≠ 6 |
| rate independent of listed seeds | skeptic.py gauge loop | any listed seed ≠ 6 |
| float is not Q | `isolate(3.0)` | no LeavesV |
| (9,6) is a collision | pair from x² seed 1 equals pair from 3x seed 2 | values differ |
| simplest traveler is fastest | time_to(0,2,8)==50,150,450 | order breaks or numbers move |
| θ=12, η=0.5 fires at 167 | until_theta | tick ≠ 167 |
| \|Bin(V3)\|=19683 | `3**9` | arithmetic |
| 113 associative on V3 labels | studio.logic / skeptic | count ≠ 113 |
| 530 frames n≤3 | modal.engine all_frames 1..3 | count ≠ 530 |
| origin composite CONDITIONAL | origin/tests/run.py | prints FORCED as composite |
| LIVE paid is generated rows | `library_verify.py` | a generator row fails |
| 95–104 are STIPULATED | those checks | they return FORCED |

Not claimed, so not falsified here:

- Riemann, Goldbach lift, P≠NP, Navier-Stokes, stars
- dual-number *formula* is original (it is the same mix; the ledger and priced `=` are the cut)
- 85 carriers are all formal systems
- a green gate is a floor under arithmetic
