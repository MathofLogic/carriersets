# All of Calc — mapped, not swallowed

This kernel is polynomials and rationals over Q-pairs.
“All of Calc” means every *chapter* gets a presentation, not that
sin lives in V=Q.

| chapter | presentation | in kernel? |
|---|---|---|
| limits | dropped; leftover named if you use fd | no — on purpose |
| definition of derivative | rate(P,G) | yes |
| power / product / quotient / chain | mix + quot + cancellation | yes |
| implicit / related / parametric | isolation policy | yes |
| inverse functions | isolate the output | yes |
| trig | init readings + jet leftover; rate(sin)=cos.v | lab `translab` |
| exp / log | init + jet leftover; rate(exp)=exp.v; log θ at 0 | lab `translab` |
| optimization | rate(f,x)=0 (output channel dead wrt x) | yes, as θ-on-rate |
| L'Hôpital | reconstructs a 0/0 *value* from live channels | yes as a warning: use rate, don't hire Inf |
| Riemann integral | listed partition extract | lab |
| FTC | rate of antiderivative vs integrand | lab |
| series | Lagrange jet / other V | jet lab is the start |
| polar / parametric | isolation | rate lab |
| multivariable | several isolators | same G, more names |
| vector calc | several isolators; grad/div/curl as rates | lab `veclab` |
| DE | constraint on channels | related-rates style |
| ε-δ proofs | unlistable V | DEFER |
| numerical fd | leftover identity | fd lab |

Full register: `docs/SCOPE.md` and `python -m pcalc.scope` (21 branches).

Grow V in public when you want sin. Do not pretend the pair did it.

Optimization sketch: `rate(f,x)=0` means f's channel died under that
isolator. A constant function already has that. A max on a listed
grid is “channel crossed 0,” not “nature peaked.”
