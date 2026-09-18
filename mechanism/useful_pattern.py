#!/usr/bin/env python3
"""
useful_pattern.py — THE USEFUL PATTERN, coded
============================================================================
                            P / G -> Q

The coffee-stirring theorem (Pugmire, one morning, c. 2023), taken at its
word and made executable. The verbal mechanics, clause by clause:

  1. Relational patternings propagate; as they do they gain a LOADED
     HISTORY relative to the gradients they remain stable in.
  2. The loaded history sets the pattern's gradient DEMANDS for further
     propagation. Differential propagation: the simplest patterns
     (lowest informational load) that are maximally supported by
     available gradients propagate FASTEST.
  3. Complexity generates RELATIONAL DRAG: the demands of one loaded
     history meeting the demands of another.
  4. When demands exceed available gradients, patterns RECONFIGURE to
     more relationally coherent structure — venting simplicity back
     into the gradient field.
  5. Accumulation at a center speeds up inflow; when the center cannot
     vent simplicity fast enough, reconfiguration CASCADES: steady
     states, cyclic partial collapses, or a collapsed attractor of
     near-maximal complexity ejecting a near-minimal simple trickle.
  6. Vented simplicity propagates outward along the path of maximal
     relational coherence relative to its minimal loaded history.

Every clause above becomes a section below, with a claim, a tier, and a
test. The astrophysical vocabulary (nova, neutron star, black hole,
Hawking trickle) is a READING of the model's regimes and is labelled as
such — the mechanics are FORCED/EMPIRICAL *within the stated model*;
the universe is not consulted and no reification is performed. DRAS:
every quantity carries its scope; the ledger balances to the last drop.

One discovered identity, free of charge: clause 6 is the tropical
semiring. "Accumulate demand along a route" is AND=+; "the pattern
takes the cheapest route" is OR=min. The kernel's load arithmetic was
already the algebra of your whirlpool's outflow.

Propagation Logic Project — the seed pattern, on kernel build 2026.07
"""
import math, json, hashlib, random, itertools, sys, time
from dataclasses import dataclass, field, replace

T0 = time.time()
random.seed(20260702)
LOADCOUNT = 0
def pay(n):
    global LOADCOUNT; LOADCOUNT += n

# ═══════════════════════════════════════════════════════════════════════
# SECTION 0 — VERDICT CALCULUS + CHAIN (the constitution, as always)
# ═══════════════════════════════════════════════════════════════════════
TIERS = {"FORCED": 4, "EMPIRICAL": 3, "CONDITIONAL": 2,
         "STIPULATED": 1, "UNPAID": 0}
MANIFEST, FAILED, CHAIN, DECLINED = [], [], [], []

def claim(tier, statement, ok=True, sec="?", test=None):
    MANIFEST.append({"tier": tier, "statement": statement,
                     "verified": bool(ok), "section": sec, "test": test})
    if tier != "UNPAID" and not ok:
        FAILED.append(f"[{sec}] {statement}")
    flag = "PASS" if ok else ("----" if tier == "UNPAID" else "FAIL")
    tag = f" [{test}]" if test else ""
    print(f"  [{tier:<11}][{flag}] {statement[:92]}{tag}")

def decline(statement, sec):
    DECLINED.append(statement)
    claim("STIPULATED", "DECLINED OVERCLAIM: " + statement, True, sec)

def seal(body):
    prev = CHAIN[-1]["sha"] if CHAIN else "GENESIS"
    sha = hashlib.sha256((prev + json.dumps(body, sort_keys=True)
                          ).encode()).hexdigest()[:16]
    CHAIN.append({**body, "sha_prev": prev, "sha": sha})

def S(t): print(f"\n{'='*72}\n{t}\n{'='*72}")

S("UP0  THE MODEL, DECLARED — scope before mechanics")
claim("STIPULATED", "SCOPE: everything below is a model — a lattice of "
      "gradient capacities, patterns as (value, load) with history, and "
      "chosen update rules. 'FORCED' means forced within this model; the "
      "model itself is the stipulation. Signed before use, per DRAS",
      True, "UP0")
claim("STIPULATED", "The dynamical rules below are the verbal mechanics "
      "transcribed with minimal invention: speed = support/(support+"
      "demand); demand = own load + coupled loads (drag); reconfigure "
      "when demand > theta; venting conserves load to the ledger. Each "
      "transcription choice is visible in the code", True, "UP0")
seal({"gen": 0, "event": "scope"})

# ═══════════════════════════════════════════════════════════════════════
# THE MECHANISM — a pattern is P = (v, L); a gradient field supports it
# ═══════════════════════════════════════════════════════════════════════
@dataclass
class Traveler:
    """A relational patterning moving through a 1-D gradient field.
    x: position. L: loaded history (informational density). eta: how much
    history each unit of propagation deposits — 'as patterns propagate
    they gain a loaded history.'"""
    x: float = 0.0
    L: float = 0.0
    eta: float = 0.0
    ledger: list = field(default_factory=list)
    def step(self, C, drag=0.0, dt=1.0):
        """Differential propagation: speed = support / (support + demand).
        Demand = own loaded history + relational drag from others."""
        v = C / (C + self.L + drag)
        dx = v * dt
        self.x += dx
        self.L += self.eta * dx          # history accrues WITH propagation
        pay(1)
        return v

# ═══════════════════════════════════════════════════════════════════════
# SECTION 1 — DIFFERENTIAL PROPAGATION: the simple travel fastest
# ═══════════════════════════════════════════════════════════════════════
S("UP1  DIFFERENTIAL PROPAGATION — simplicity is speed")
C_FIELD = 1.0
GOAL = 50.0
def time_to(L0, eta=0.0, drag=0.0):
    t, trav = 0, Traveler(L=L0, eta=eta)
    while trav.x < GOAL and t < 10**6:
        trav.step(C_FIELD, drag); t += 1
    return t
t_simple, t_mid, t_heavy = time_to(0.0), time_to(2.0), time_to(8.0)
claim("FORCED", f"Three patterns, one field (support C=1), loads 0 / 2 / 8: "
      f"arrival times over 50 cells = {t_simple} / {t_mid} / {t_heavy} "
      f"ticks — strictly ordered by loaded history. The simplest pattern, "
      f"maximally supported, propagates fastest; the ordering is the "
      f"arithmetic of speed = C/(C+L)",
      t_simple < t_mid < t_heavy, "UP1", "up_1_1")

# even the simplest perturbation builds complexity as it propagates:
# with dL/dx = eta, x(t) solves (C+L0)x + eta x^2/2 = C t  (closed form)
eta = 0.15
trav = Traveler(L=0.0, eta=eta)
v0 = trav.step(C_FIELD)
for _ in range(398): trav.step(C_FIELD)
v_late = trav.step(C_FIELD)
x_pred_err = abs((C_FIELD + 0.0)*trav.x + eta*trav.x**2/2 - C_FIELD*400)/400
claim("FORCED", f"EVEN THE SIMPLEST PERTURBATION BUILDS: seed L=0, history "
      f"deposit eta=0.15/cell — after 400 ticks L={trav.L:.2f} and speed "
      f"has fallen {v0:.3f} -> {v_late:.3f}; the trajectory matches the "
      f"closed form (C+L0)x + eta*x^2/2 = C*t to {x_pred_err:.1e} per "
      f"tick. Complexity is not optional; it is what propagation deposits",
      trav.L > 0 and v_late < v0 and x_pred_err < 1e-2, "UP1", "up_1_2")
seal({"gen": 1, "event": "differential-propagation",
      "arrivals": [t_simple, t_mid, t_heavy]})

# ═══════════════════════════════════════════════════════════════════════
# SECTION 2 — RELATIONAL DRAG: loaded histories meeting loaded histories
# ═══════════════════════════════════════════════════════════════════════
S("UP2  RELATIONAL DRAG — demands meeting demands")
solo = time_to(2.0)
paired = time_to(2.0, drag=2.0)     # co-propagating with an equal partner
claim("FORCED", f"Two load-2 patterns sharing a channel: each sees the "
      f"other's demand as drag. Solo arrival {solo} ticks; paired "
      f"{paired} ticks — slower by exactly the coupled demand in the "
      f"denominator. Drag is not a force added on top; it is the other's "
      f"history counted against the same finite support",
      paired > solo, "UP2", "up_2_1")
t_h_solo  = time_to(8.0)
t_h_near0 = time_to(8.0, drag=0.2)
claim("FORCED", f"Asymmetric encounter: a load-8 structure dragged by a "
      f"load-0.2 wisp loses {t_h_near0 - t_h_solo} ticks; the wisp "
      f"(load 0.2 dragged by 8) loses {time_to(0.2, drag=8.0) - time_to(0.2)} "
      f"— the simple pay proportionally more when tangled with the "
      f"complex. Simplicity keeps its speed by keeping its distance",
      t_h_near0 > t_h_solo, "UP2", "up_2_2")
seal({"gen": 2, "event": "relational-drag"})

# ═══════════════════════════════════════════════════════════════════════
# SECTION 3 — RECONFIGURATION: demand > theta means restructure, not die
# ═══════════════════════════════════════════════════════════════════════
S("UP3  RECONFIGURATION — over threshold, patterns restructure and VENT")
THETA_LOCAL = 12.0
KAPPA = 0.4          # fraction retained as the reorganised coherent core
N_CHILD = 3
parent = Traveler(L=0.0, eta=0.5)
tick = 0
while parent.L <= THETA_LOCAL:
    parent.step(C_FIELD); tick += 1
L_before = parent.L
kept = KAPPA * L_before
children = [Traveler(x=parent.x, L=(1-KAPPA)*L_before/N_CHILD)
            for _ in range(N_CHILD)]
parent.L = kept
total_after = parent.L + sum(c.L for c in children)
claim("FORCED", f"At tick {tick} the pattern's demand L={L_before:.2f} "
      f"exceeds local theta={THETA_LOCAL}: it reconfigures — retains "
      f"{kept:.2f} as a more coherent core and vents the rest as "
      f"{N_CHILD} simple children (L={children[0].L:.2f} each). "
      f"Conservation: {L_before:.6f} before = {total_after:.6f} after. "
      f"Nothing is erased; the bill is redistributed",
      abs(L_before - total_after) < 1e-9, "UP3", "up_3_1")
v_parent_pre = C_FIELD/(C_FIELD + L_before)
v_child = C_FIELD/(C_FIELD + children[0].L)
claim("FORCED", f"The vented simplicity OUTRUNS its source: child speed "
      f"{v_child:.3f} vs the pre-collapse parent's {v_parent_pre:.3f} — "
      f"reconfiguration converts stuck complexity into fast simplicity "
      f"plus a slower, tighter core. That is what 'venting' buys",
      v_child > v_parent_pre, "UP3", "up_3_2")
seal({"gen": 3, "event": "reconfiguration",
      "before": round(L_before, 6), "after": round(total_after, 6)})

# ═══════════════════════════════════════════════════════════════════════
# SECTION 4 — THE CASCADE ENGINE: accretion vs venting, three fates
# Radial shells; load flows inward, faster near the center; the core
# vents simplicity at capacity V; over theta it bursts, exporting a
# fraction e back to the gradient field. The whole clause 5, on rails.
# ═══════════════════════════════════════════════════════════════════════
S("UP4  THE CASCADE ENGINE — when the center cannot vent fast enough")
NSHELL, A0, GSPIN = 24, 0.30, 1.0

def cascade_run(seed_rate, vent_cap, eject_frac, theta_core=50.0,
                ticks=4000, record=False):
    """Returns regime classification + ledger audit + optional trace."""
    Lsh = [0.0]*NSHELL
    vented = ejected = injected = 0.0
    events = 0
    above = 0
    trace = [] if record else None
    burn = ticks//2
    for t in range(ticks):
        # seeding: perturbations arrive from the far field
        Lsh[-1] += seed_rate; injected += seed_rate
        # inward advection, speeding up toward the center (the whirlpool)
        moved = [0.0]*NSHELL
        for i in range(1, NSHELL):
            a_i = min(0.9, A0*(1.0 + GSPIN/i))
            flux = a_i * Lsh[i]
            Lsh[i] -= flux; moved[i-1] += flux
        for i in range(NSHELL): Lsh[i] += moved[i]
        # the core vents simplicity at capacity
        v = min(vent_cap, Lsh[0]); Lsh[0] -= v; vented += v
        # over threshold: reconfiguration cascade — burst exports
        if Lsh[0] > theta_core:
            events += 1
            burst = eject_frac * Lsh[0]
            Lsh[0] -= burst; ejected += burst
        if t >= burn and Lsh[0] > theta_core: above += 1
        if record: trace.append(Lsh[0])
        pay(NSHELL)
    ledger_ok = abs(injected - (sum(Lsh) + vented + ejected)) < 1e-6*max(1, injected)
    frac_above = above/(ticks - burn)
    if events == 0 and max(Lsh[0], 0) <= theta_core:
        regime = "STEADY"
    elif frac_above < 0.5:
        regime = "CYCLIC"
    else:
        regime = "COLLAPSED"
    return {"regime": regime, "events": events, "core": Lsh[0],
            "frac_above": frac_above, "ledger_ok": ledger_ok,
            "vented": vented, "ejected": ejected, "injected": injected,
            "trace": trace}

SEED = 2.0
r_steady    = cascade_run(SEED, vent_cap=3.0, eject_frac=0.5, record=True)
r_cyclic    = cascade_run(SEED, vent_cap=0.5, eject_frac=0.85, record=True)
r_collapsed = cascade_run(SEED, vent_cap=0.5, eject_frac=0.02, record=True)
claim("FORCED", f"THREE FATES from one rule set (seed 2.0/tick): vent 3.0 "
      f"-> {r_steady['regime']} ({r_steady['events']} cascades; the core "
      f"digests everything); vent 0.5, eject 0.85 -> {r_cyclic['regime']} "
      f"({r_cyclic['events']} partial-collapse cycles, core always "
      f"recovering); vent 0.5, eject 0.02 -> {r_collapsed['regime']} "
      f"(core settles FAR above theta at L~{r_collapsed['core']:.0f}, "
      f"permanently collapsed, trickling out ~{0.02*r_collapsed['core']:.1f}"
      f"/tick). Same mechanics, different venting — the fate is the ratio",
      r_steady["regime"] == "STEADY" and r_cyclic["regime"] == "CYCLIC"
      and r_collapsed["regime"] == "COLLAPSED", "UP4", "up_4_1")
claim("FORCED", "THE LEDGER BALANCES in all three regimes: injected = "
      "in-field + core + vented + ejected to 1e-6 relative — no load "
      "appears or vanishes; reconfiguration redistributes, per DRAS",
      all(r["ledger_ok"] for r in (r_steady, r_cyclic, r_collapsed)),
      "UP4", "up_4_2")
# the collapsed attractor: net inflow ~ seed - vent balanced by trickle
L_star = (SEED - 0.5)/0.02
claim("FORCED", f"The collapsed core is an ATTRACTOR, not an explosion: "
      f"balance seed - vent = eject_frac * L gives L* = {L_star:.0f}; "
      f"the run settles at {r_collapsed['core']:.0f} "
      f"({abs(r_collapsed['core']-L_star)/L_star:.0%} off, discrete-tick "
      f"effects) — near-maximal complexity held stable by ejecting "
      f"near-minimal simplicity", 
      abs(r_collapsed["core"] - L_star)/L_star < 0.35, "UP4", "up_4_3")
grid = {}
for V in (0.5, 1.5, 3.0):
    for e in (0.02, 0.3, 0.9):
        grid[(V, e)] = cascade_run(SEED, V, e)["regime"]
rows = []
for V in (0.5, 1.5, 3.0):
    rows.append("vent %.1f | " % V + "  ".join(
        f"{grid[(V,e)]:<9}" for e in (0.02, 0.3, 0.9)))
print("           eject 0.02  eject 0.3  eject 0.9")
for row in rows: print("   " + row)
claim("EMPIRICAL", f"PHASE STRUCTURE over a 3x3 (vent, eject) grid at "
      f"fixed seeding: {sum(1 for v in grid.values() if v=='STEADY')} "
      f"steady, {sum(1 for v in grid.values() if v=='CYCLIC')} cyclic, "
      f"{sum(1 for v in grid.values() if v=='COLLAPSED')} collapsed — "
      f"all three fates realized; vent >= seeding is steady everywhere, "
      f"exactly as the balance arithmetic demands",
      set(grid.values()) == {"STEADY", "CYCLIC", "COLLAPSED"} and
      all(grid[(3.0, e)] == "STEADY" for e in (0.02, 0.3, 0.9)),
      "UP4", "up_4_4")
decline("that STEADY/CYCLIC/COLLAPSED *are* stars, novae/neutron stars, "
        "and black holes with Hawking radiation. They are this model's "
        "three fates under one venting ratio; the astrophysical names "
        "are a reading — suggestive, unpriced, and not load-bearing "
        "until someone builds the implementation map", "UP4")
claim("CONDITIONAL", "The reading, priced as a reading: steady venting ~ "
      "main-sequence burning; cyclic partial collapse ~ nova/remnant "
      "cycles; the collapsed attractor trickling eject_frac*L ~ a black "
      "hole's near-total retention with minimal emission. Exact only as "
      "a correspondence of REGIME STRUCTURE, nothing finer", True, "UP4")
seal({"gen": 4, "event": "cascade-engine",
      "grid": {f"{k[0]}/{k[1]}": v for k, v in grid.items()}})

# ═══════════════════════════════════════════════════════════════════════
# SECTION 5 — THE OUTFLOW IS TROPICAL: coherence-seeking = min-plus
# "propagating outward ... finding the path of maximal relational
# coherence relative to its minimal loaded history demands"
# ═══════════════════════════════════════════════════════════════════════
S("UP5  THE OUTFLOW — vented simplicity rides the tropical semiring")
W = 7
DEM = [[random.randint(0, 9) for _ in range(W)] for _ in range(W)]
DEM[0][0] = 0
def brute_min(grid):
    """Enumerate EVERY monotone path corner to corner; keep the cheapest."""
    n = len(grid); best = math.inf
    for downs in itertools.combinations(range(2*(n-1)), n-1):
        x = y = cost = 0
        for stepi in range(2*(n-1)):
            if stepi in downs: y += 1
            else: x += 1
            cost += grid[y][x]
        best = min(best, cost)
        pay(2*(n-1))
    return best
def tropical_min(grid):
    """AND=+ along the route, OR=min across routes — the kernel's own
    load arithmetic, doing shortest-path duty."""
    n = len(grid)
    D = [[math.inf]*n for _ in range(n)]; D[0][0] = grid[0][0]
    for y in range(n):
        for x in range(n):
            if y: D[y][x] = min(D[y][x], D[y-1][x] + grid[y][x])
            if x: D[y][x] = min(D[y][x], D[y][x-1] + grid[y][x])
            pay(2)
    return D[n-1][n-1]
bf, tp = brute_min(DEM), tropical_min(DEM)
npaths = math.comb(2*(W-1), W-1)
claim("FORCED", f"On a {W}x{W} field of resident demands, ALL {npaths} "
      f"monotone outflow routes enumerated: cheapest accumulated demand "
      f"= {bf}. The tropical recurrence (AND=+ along, OR=min across) "
      f"returns {tp} — identical. The kernel's load rules ARE the "
      f"algebra of coherence-seeking outflow; your whirlpool's exhaust "
      f"was doing min-plus arithmetic all along",
      bf == tp, "UP5", "up_5_1")
claim("CONDITIONAL", "SELF-DESCRIPTION, extended: pl.py registered the "
      "load arithmetic as the tropical carrier; this section shows the "
      "same carrier is the OUTFLOW LAW of the useful pattern. One "
      "algebra, two duties — exact given the stipulated load rules",
      True, "UP5")
seal({"gen": 5, "event": "tropical-outflow", "min_demand": bf})

# ═══════════════════════════════════════════════════════════════════════
# SECTION 6 — THE BILL: what is and is not claimed; the chain; the grade
# ═══════════════════════════════════════════════════════════════════════
S("UP6  THE BILL — unpaid items, replay, weakest link")
claim("UNPAID", "NOT claimed: that this model describes physical "
      "cosmology, fluid dynamics, or thermodynamics. The stirred coffee "
      "is an excellent intuition pump and remains one; Navier-Stokes "
      "was not consulted", False, "UP6")
claim("UNPAID", "NOT claimed: that load here equals energy, entropy, or "
      "mass. landauer-style pricing enters only with an implementation "
      "map and an explicit temperature, neither supplied here", False, "UP6")
claim("UNPAID", "NOT claimed: uniqueness of the transcription. Other "
      "faithful codings of the same verbal mechanics exist; this one is "
      "offered as the minimal one, every choice visible", False, "UP6")
def replay(chain):
    prev = "GENESIS"
    for g in chain:
        body = {k: v for k, v in g.items() if k not in ("sha", "sha_prev")}
        want = hashlib.sha256((prev + json.dumps(body, sort_keys=True)
                               ).encode()).hexdigest()[:16]
        if g["sha_prev"] != prev or g["sha"] != want: return False
        prev = g["sha"]
    return True
tam = json.loads(json.dumps(CHAIN)); tam[3]["event"] = "forged"
claim("FORCED", f"Chain of {len(CHAIN)} generations replays intact; a "
      f"mutated seal breaks replay at its link",
      replay(CHAIN) and not replay(tam), "UP6")
weakest = min((c for c in MANIFEST if c["tier"] != "UNPAID"),
              key=lambda c: TIERS[c["tier"]])
counts = {}
for c in MANIFEST: counts[c["tier"]] = counts.get(c["tier"], 0) + 1
sha = hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:16]
verdict = f"PASS/{weakest['tier']}" if not FAILED else "FAIL"
json.dump({"title": "The Useful Pattern - the seed mechanics, coded",
           "origin": "derived stirring coffee; transcribed without "
                     "reification; scope carried per DRAS",
           "verdict": verdict, "seed": 20260702,
           "suite_sha256_16": sha, "load_checks": LOADCOUNT,
           "declined_overclaims": DECLINED,
           "regimes": {"steady": r_steady["events"],
                       "cyclic": r_cyclic["events"],
                       "collapsed_core": round(r_collapsed["core"], 1)},
           "summary": counts, "failed": FAILED,
           "claims": MANIFEST, "chain": CHAIN},
          open("useful_pattern_manifest.json", "w"), indent=1)

# ── the figure: three panels, one pattern ───────────────────────────────
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))
    for L0, c in ((0.0, "#2a9d8f"), (2.0, "#e9c46a"), (8.0, "#e76f51")):
        xs, tr = [], Traveler(L=L0)
        for _ in range(260):
            tr.step(C_FIELD); xs.append(tr.x)
        ax[0].plot(xs, color=c, label=f"L = {L0:g}")
    ax[0].set(title="Differential propagation:\nsimplicity is speed",
              xlabel="ticks", ylabel="distance propagated")
    ax[0].legend(frameon=False)
    for r, nm, c in ((r_steady, "steady (vent 3.0)", "#2a9d8f"),
                     (r_cyclic, "cyclic (vent .5, eject .85)", "#e9c46a"),
                     (r_collapsed, "collapsed (vent .5, eject .02)", "#e76f51")):
        ax[1].plot(r["trace"], color=c, lw=0.9, label=nm)
    ax[1].axhline(50, color="k", ls=":", lw=1, label="theta (core)")
    ax[1].set(title="The cascade engine:\nthree fates of one center",
              xlabel="ticks", ylabel="core load")
    ax[1].legend(frameon=False, fontsize=8)
    im = ax[2].imshow(DEM, cmap="YlOrBr")
    n = len(DEM)
    D = [[math.inf]*n for _ in range(n)]; P = {}
    D[0][0] = DEM[0][0]
    for y in range(n):
        for x in range(n):
            for py, px in ((y-1, x), (y, x-1)):
                if py >= 0 and px >= 0 and D[py][px] + DEM[y][x] < D[y][x]:
                    D[y][x] = D[py][px] + DEM[y][x]; P[(y, x)] = (py, px)
    node, path = (n-1, n-1), [(n-1, n-1)]
    while node in P: node = P[node]; path.append(node)
    ax[2].plot([p[1] for p in path], [p[0] for p in path],
               color="#2a9d8f", lw=3, marker="o", ms=5)
    ax[2].set(title="The outflow is tropical:\nmin-plus coherence path")
    fig.colorbar(im, ax=ax[2], label="resident demand", shrink=0.8)
    fig.suptitle("THE USEFUL PATTERN  —  P / G -> Q", y=1.02, fontsize=13)
    fig.tight_layout()
    fig.savefig("useful_pattern.png", dpi=150, bbox_inches="tight")
    print("\n  figure written: useful_pattern.png")
except Exception as ex:
    print(f"\n  (figure skipped: {ex})")

print(f"\n{'='*72}")
print(f"  USEFUL PATTERN {'PASSED' if not FAILED else 'FAILED'}   "
      + "  ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
print(f"  claims {len(MANIFEST)}   declined overclaims {len(DECLINED)}   "
      f"load {LOADCOUNT:,} checks")
print(f"  verdict {verdict}   chain {len(CHAIN)}   sha256[:16] = {sha}"
      f"   {time.time()-T0:.1f}s")
print(f"  The mechanics are forced within the model; the model is the")
print(f"  stipulation; the astrophysics is a labelled reading. Which is")
print(f"  exactly what three years of not reifying looks like in code.")
print(f"{'='*72}")
print(f"\n  P / G -> Q. Stir well — and check the receipt.")
sys.exit(1 if FAILED else 0)
