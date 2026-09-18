"""A mark that moves and loads. Not two marks identified at birth."""


class Traveler:
    __slots__ = ("x", "L", "eta", "tag")

    def __init__(self, x=0.0, L=0.0, eta=0.0, tag=""):
        self.x = float(x)
        self.L = float(L)
        self.eta = float(eta)
        self.tag = tag

    def step(self, C, drag=0.0, dt=1.0):
        v = C / (C + self.L + drag)
        dx = v * dt
        self.x += dx
        self.L += self.eta * dx
        return v


def time_to(L0, C=1.0, goal=50.0, cap=10 ** 6):
    tr = Traveler(L=L0)
    t = 0
    while tr.x < goal and t < cap:
        tr.step(C)
        t += 1
    return t


def until_theta(eta, theta, C=1.0, cap=10 ** 6):
    tr = Traveler(eta=eta)
    t = 0
    while tr.L <= theta and t < cap:
        tr.step(C)
        t += 1
    return t, tr
