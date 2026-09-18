import sys
from studio import algebra, calc, eq, logic, steps


def main():
    print("STUDIO")
    print()
    algebra.main()
    print()
    logic.main()
    print()
    calc.main()
    print()
    steps.main()
    print()
    eq.main()
    print()
    print("verdict PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
