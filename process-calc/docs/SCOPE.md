# Calculus domain register

```
PYTHONPATH=process-calc:. python3 -m pcalc.scope
```

Every branch is a cut: closes on Q, or leftover / θ / grow-V is named.
This is not “all of analysis lives in PROCESS.py.”

| # | branch | cut | status |
|---|---|---|---|
| 1 | single-var | rate, mix, quot, chain | Q |
| 2 | inverse | isolate the output | Q |
| 3 | implicit / related | dead constraint channel | Q |
| 4 | parametric / polar | rate/rate of two readings | Q |
| 5 | inv-trig / hyperbolic | init + jet | grow V |
| 6 | optimization | rate=0 | Q |
| 7 | L'Hôpital | 0/0 value θ; live channels still ratio | use rate |
| 8 | Riemann / FTC | listed grid extract | leftover |
| 9 | series / radius | jet; leave V is θ | leftover |
| 10 | partials / Hessian | several isolators; Hessian later slot | Q + slot |
| 11 | directional / Jacobian | seed is the direction | Q |
| 12 | line integral | rate along path, then grid | Q + extract |
| 13 | Green / Stokes / div | two extracts agree | veclab |
| 14 | ODE | rate constraint on a reading | Q |
| 15 | PDE | two isolators + r2 slot | jetlab |
| 16 | variations | rate of action wrt path-slot | extra name |
| 17 | Fourier / Laplace | listed mesh extract | grid |
| 18 | complex / CR | wrap i; two isolators | other V |
| 19 | finite difference | leftover vs rate | fdlab |
| 20 | fractional / SDE / distributions / NSA | other G or Inf-as-V | DEFER |
| 21 | exterior forms | d²=0 is curl-grad packing | packing |

Labs: `translab` `veclab` `jetlab` `fdlab` `intlab` `ftclab` `ratelab`.
