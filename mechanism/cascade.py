"""One core. Seed, vent, eject. Three fates. Ledger must close."""


def run(seed, vent, eject, theta=50.0, ticks=800):
    L = 0.0
    injected = vented = ejected = 0.0
    events = 0
    above = 0
    burn = ticks // 2
    for t in range(ticks):
        L += seed
        injected += seed
        v = min(vent, L)
        L -= v
        vented += v
        if L > theta:
            events += 1
            burst = eject * L
            L -= burst
            ejected += burst
        if t >= burn and L > theta:
            above += 1
    frac = above / (ticks - burn) if ticks > burn else 0
    if events == 0:
        regime = "STEADY"
    elif frac < 0.5:
        regime = "CYCLIC"
    else:
        regime = "COLLAPSED"
    ledger = abs(injected - (L + vented + ejected))
    return {
        "regime": regime,
        "events": events,
        "core": L,
        "ledger": ledger,
        "injected": injected,
        "vented": vented,
        "ejected": ejected,
    }


def vent_split(L, kappa, n=3):
    kept = kappa * L
    kids = [(1 - kappa) * L / n] * n
    return kept, kids
