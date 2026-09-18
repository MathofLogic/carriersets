# Ops to output

Claim you can check:

For f(x)=x^2 at x=3, the pair path reaches 6 in 5 arithmetic
operations on Q. The school difference-quotient path reaches 6+h
in 5 arithmetic operations. Getting from 6+h to 6 is not an
operation on Q. It is a limit step imported from another cut.

```
PYTHONPATH=. python3 -m studio.steps
```

```
pair rate          ops=5  value=6
  *  3 3 -> 9
  *  3 1 -> 3
  *  1 3 -> 3
  +  3 3 -> 6
  /  6 1 -> 6

fd h=1/2           ops=5  value=13/2  leftover=1/2
school to 6+h      ops=5  value=13/2
```

Falsifier: a finite list of + * / on Q, no limit, no Inf, no
"set h=0 after dividing by h", that sends (f(3+h)-f(3))/h to 6
for a generic h.

"Easier" here is that count. 5 ops and you have 6. The other path
uses 5 ops and still owes a step this V does not contain.
That owed step is what "approach but never reach" is asking a
15-year-old to accept before they multiply.
