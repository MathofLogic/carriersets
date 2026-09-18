# Algebra domain register

```
PYTHONPATH=process-calc:. python3 -m pcalc.algscope
PYTHONPATH=. python3 -m studio.algebra
```

| # | branch | cut | status |
|---|---|---|---|
| 1 | magma / monoid | enumerate assoc + id | ENUM |
| 2 | groups | S3 order 6 not abelian | ENUM |
| 3 | rings Z/n | units listed | ENUM |
| 4 | fields | fieldish n=2..12 primes | ENUM |
| 5 | integral domain | Z/4 zero-divisors (2,2) | ENUM |
| 6 | polynomials Q | eval Reading | Q |
| 7 | linear solve | search listed V | SEARCH |
| 8 | matrices | det; singular is θ | Q |
| 9 | inverse 2×2 | adjugate / det | Q+θ |
| 10 | eigen | char poly; roots on listed Q | Q |
| 11 | quotients | wrap tick | WRAP |
| 12 | lattices | min/max closed V3 | ENUM |
| 13 | Boolean | V2 min/max | ENUM |
| 14 | homomorphisms | mod-3 preserves + | ENUM |
| 15 | tropical | min-plus | ENUM |
| 16 | geometric algebra 2d | bivector wrap | mini |
| 17 | gcd | Euclid search | SEARCH |
| 18 | generating functions | jet at 0 | Q |
| 19 | Lie / reps / AG / homology | other V | DEFER |
| 20 | letters | holes, not boxes | REWRITE |

Calc register: `docs/SCOPE.md`. Together they are the domain map, not the terrain.
