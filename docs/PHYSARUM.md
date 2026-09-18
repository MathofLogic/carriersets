# Physarum net

The dish HTML is a program. This folder runs a smaller copy and
extracts food-to-food links. It does not instantiate a slime.

```
V      cond, chem, rich on listed cells
G      sense, deposit, return-flow, decay
theta  off-dish, energy 0, cond below cut
```

Forward chem = nutrient isolation.
Return rich = well-fed isolation the other way.
cond = loaded history. Tubes hold while support holds.

Tokyo subway technique: food marks on a dish, conductance grows,
read the tubes. No Dijkstra library. No JAX.

AD is one G (Leibniz mix on Q-pairs). This is another G (field +
agents). Neither is the only machine. Both refuse silent V-growth
if you keep theta.

```
PYTHONPATH=. python3 tools/physarum_net.py
```

Open `tools/slime_dish.html` in a browser for the live dish.
