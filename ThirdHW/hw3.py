"""Решение линейных диофантовых уравнений расширенным алгоритмом Евклида."""

import sys


def extended_gcd(a, b):
    """Вернуть (d, x, y), где a*x + b*y = d = НОД(a, b)."""
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    return d, y1, x1 - (a // b) * y1


def solve(a, b):
    """Вернуть (x, y, d) с минимальным |x| + |y|, затем минимальным x."""
    d, x0, y0 = extended_gcd(a, b)
    step_x = b // d
    step_y = a // d

    best_x, best_y = x0, y0
    best_key = (abs(x0) + abs(y0), x0)

    for k in range(-2, 3):
        x = x0 + step_x * k
        y = y0 - step_y * k
        key = (abs(x) + abs(y), x)
        if key < best_key:
            best_key = key
            best_x, best_y = x, y

    return best_x, best_y, d


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        x, y, d = solve(a, b)
        print(x, y, d)


if __name__ == "__main__":
    main()