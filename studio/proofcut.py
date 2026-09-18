"""proofcut — cheapest next check, not a proof factory.

A conjecture is a sentence plus a V. Most of the bill is the lift off
a finite cut. This file prices the cut and names the lift. It does not
sell the lift as paid.

    PYTHONPATH=. python3 -m studio.proofcut
"""
from __future__ import annotations

import time


def primes_upto(n):
    s = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = [False] * len(s[i * i::i])
    return [i for i, p in enumerate(s) if p]


def goldbach(M=2000):
    P = set(primes_upto(M))
    evens = range(4, M + 1, 2)
    miss = [n for n in evens
            if not any((n - p) in P for p in P if p <= n - 2)]
    return {"cut": f"even 4..{M}", "n": (M - 2) // 2, "miss": miss,
            "lift": "all even n>=4. induction/schema. unpaid here."}


def collatz(N=2000, bound=500):
    miss = []
    for n in range(1, N + 1):
        x, k, seen = n, 0, set()
        while x != 1 and k < bound and x not in seen:
            seen.add(x)
            x = x // 2 if x % 2 == 0 else 3 * x + 1
            k += 1
        if x != 1:
            miss.append(n)
    return {"cut": f"n=1..{N} steps<{bound}", "n": N, "miss": miss,
            "lift": "all n, unbounded traces. unpaid here."}


def twins(M=5000):
    P = primes_upto(M)
    S = set(P)
    k = sum(1 for p in P if p + 2 in S)
    return {"cut": f"p<= {M}", "n": k, "miss": [],
            "lift": "infinitely many. unpaid here."}


def fermat(N=20, nmax=5):
    hits = []
    for n in range(3, nmax + 1):
        for a in range(1, N + 1):
            for b in range(a, N + 1):
                s = a ** n + b ** n
                c = round(s ** (1 / n))
                if 1 <= c <= N and c ** n == s:
                    hits.append((a, b, c, n))
    return {"cut": f"a,b,c<= {N} n=3..{nmax}", "n": N * N * (nmax - 2),
            "miss": hits, "lift": "all a,b,c,n>2. FLT is not this cut."}


def protocol(name, row, dt):
    status = "BREAK" if row["miss"] else "FORCED-on-cut"
    print(f"{name:<10} {status:<16} {row['cut']:<28} "
          f"checked={row['n']:<6} {dt*1000:6.1f} ms")
    print(f"           lift: {row['lift']}")
    if row["miss"]:
        print(f"           witness: {row['miss'][:8]}")


def main():
    print("PROOFCUT  price the cut, name the lift")
    print()
    t = time.perf_counter(); g = goldbach(); protocol("GOLDBACH", g, time.perf_counter()-t)
    t = time.perf_counter(); c = collatz(); protocol("COLLATZ", c, time.perf_counter()-t)
    t = time.perf_counter(); w = twins(); protocol("TWINS", w, time.perf_counter()-t)
    t = time.perf_counter(); f = fermat(); protocol("FERMAT", f, time.perf_counter()-t)
    print()
    print("cheap next move, in this order:")
    print("  1 write V G theta for the sentence. if you cannot, not a claim yet")
    print("  2 search a BREAK on the smallest cut that could host one")
    print("  3 if no break, you have FORCED-on-cut. stop calling it a proof")
    print("  4 name the lift (schema, compactness, continuation). price it")
    print("  5 only then spend search on the lift's own carrier")
    print()
    print("this does not solve Riemann. it stops paying Riemann-prices")
    print("for a sentence that already dies at n=1.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
