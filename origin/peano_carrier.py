"""Axiomatic route. Posited 0 and S. + and * by recursion on S."""


class Nat:
    __slots__ = ("k",)

    def __init__(self, k):
        if k < 0:
            raise ValueError("Nat is the non-negative cut")
        self.k = k

    def __int__(self):
        return self.k

    def __eq__(self, o):
        return isinstance(o, Nat) and self.k == o.k

    def __repr__(self):
        return f"Nat({self.k})"


Z = Nat(0)


def S(n):
    return Nat(n.k + 1)


def nat(k):
    return Nat(k)


def add(a, b):
    if b.k == 0:
        return a
    return S(add(a, Nat(b.k - 1)))


def mul(a, b):
    if b.k == 0:
        return Z
    return add(mul(a, Nat(b.k - 1)), a)
