"""Outflow G. min-plus is one row. Cousins exist."""


def min_plus(grid):
    n = len(grid)
    D = [[float("inf")] * n for _ in range(n)]
    D[0][0] = grid[0][0]
    for y in range(n):
        for x in range(n):
            if y:
                D[y][x] = min(D[y][x], D[y - 1][x] + grid[y][x])
            if x:
                D[y][x] = min(D[y][x], D[y][x - 1] + grid[y][x])
    return D[-1][-1]


def brute_monotone(grid):
    import itertools
    n = len(grid)
    best = float("inf")
    need = n - 1
    for downs in itertools.combinations(range(2 * need), need):
        x = y = 0
        cost = grid[0][0]
        for i in range(2 * need):
            if i in downs:
                y += 1
            else:
                x += 1
            cost += grid[y][x]
        if cost < best:
            best = cost
    return best
