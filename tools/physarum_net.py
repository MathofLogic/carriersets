"""Physarum-style network on a listed grid.

Tokyo-subway technique as a program, not a creature.

V      conductance on dish cells; listed food marks
G      deposit, decay, sense, return-flow
theta  off-dish, energy 0, conductance below KTHRESH

Forward chem is nutrient isolation.
Return rich is well-fed isolation the other way.
cond is loaded history. Tubes persist while C holds.

No AD library. No shortest-path library.
Output: food-to-food links where cond stays above a cut.

    PYTHONPATH=. python3 tools/physarum_net.py
"""
from __future__ import annotations

import math
import random

GW = GH = 48
CX = CY = GW / 2
DR = GW * 0.46
KTHRESH = 0.05
KDEP = 0.02
KDECAY = 0.997
CDECAY = 0.88
RDECAY = 0.90
STEPS = 180
AGENTS = 400


def in_dish(x, y):
    return (x - CX) ** 2 + (y - CY) ** 2 < (DR - 1) ** 2


def idx(x, y):
    return int(y) * GW + int(x)


def run(foods=None, seed=1):
    random.seed(seed)
    n = GW * GH
    chem = [0.0] * n
    rich = [0.0] * n
    cond = [0.06 if in_dish(x, y) else 0.0 for y in range(GH) for x in range(GW)]
    if foods is None:
        foods = [
            (CX + (rx - 0.5) * DR * 1.6, CY + (ry - 0.5) * DR * 1.6)
            for rx, ry in ((0.28, 0.28), (0.72, 0.28), (0.5, 0.82), (0.5, 0.5))
        ]
    foods = [(fx, fy) for fx, fy in foods if in_dish(fx, fy)]
    agents = []
    while len(agents) < AGENTS:
        x, y = random.random() * GW, random.random() * GH
        if in_dish(x, y):
            agents.append([x, y, random.random() * math.tau, 80.0])

    def sense(x, y, a):
        sx = int(x + math.cos(a) * 3)
        sy = int(y + math.sin(a) * 3)
        if not (0 <= sx < GW and 0 <= sy < GH) or not in_dish(sx, sy):
            return -8.0
        i = idx(sx, sy)
        if cond[i] < KTHRESH:
            return -8.0
        fwd = chem[i] * (0.1 + 0.9 * min(1.0, cond[i] / 0.25))
        return fwd if fwd > 4 else fwd + rich[i] * 0.3

    for _ in range(STEPS):
        nc = [chem[i] * CDECAY if in_dish(i % GW, i // GW) else 0.0 for i in range(n)]
        nr = [rich[i] * RDECAY if in_dish(i % GW, i // GW) else 0.0 for i in range(n)]
        for fx, fy in foods:
            i = idx(fx, fy)
            if 0 <= i < n:
                nc[i] = min(80.0, nc[i] + 18.0)
        for ag in agents:
            x, y, a, e = ag
            if e <= 0:
                continue
            f, l, r = sense(x, y, a), sense(x, y, a - 0.4), sense(x, y, a + 0.4)
            if not (f >= l and f >= r):
                if l > r:
                    a -= 0.7
                elif r > l:
                    a += 0.7
                else:
                    a += 0.7 if random.random() > 0.5 else -0.7
            x += math.cos(a)
            y += math.sin(a)
            if not in_dish(x, y):
                a += math.pi
                x, y = CX + (x - CX) * 0.9, CY + (y - CY) * 0.9
            ix, iy = int(x), int(y)
            if in_dish(ix, iy):
                i = idx(ix, iy)
                cond[i] = min(1.0, cond[i] + KDEP)
                cond[i] *= KDECAY
                nc[i] = min(80.0, nc[i] + 1.2)
                if e > 50:
                    nr[i] = min(80.0, nr[i] + 2.0)
                e = min(120.0, e + nc[i] * 0.02 - 0.15)
            else:
                e -= 0.4
            ag[:] = [x, y, a, e]
        chem, rich = nc, nr

    links = []
    for i, a in enumerate(foods):
        for j, b in enumerate(foods):
            if j <= i:
                continue
            steps = 16
            acc = []
            for t in range(steps + 1):
                u = t / steps
                x, y = a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u
                if in_dish(x, y):
                    acc.append(cond[idx(x, y)])
            if not acc:
                continue
            mean = sum(acc) / len(acc)
            if mean >= 0.88:
                links.append((i, j, round(mean, 3)))
    return {"foods": foods, "links": links, "tube_cells": sum(1 for c in cond if c >= KTHRESH)}


def main():
    print("PHYSARUM NET  bidirectional field, no AD lib")
    out = run()
    print(f"  foods {len(out['foods'])}  tube_cells {out['tube_cells']}")
    print(f"  links {out['links']}")
    print("  V=cond+chem+rich  G=sense/deposit/return  theta=off-dish/KTHRESH")
    print("  this is a map of a process already running in the dish HTML.")
    print("verdict PASS" if out["links"] else "verdict SPARSE")
    return 0 if out["links"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
