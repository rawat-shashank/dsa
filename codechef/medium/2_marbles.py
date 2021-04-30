# Solution => Beggar's method

# NCR = > N = (n-1), R = n-k
# NCR = (n-1) C(n-k)

# C(n, r) = (n-1)!((n-k)!((n-1)−(n-k))!)

import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def main():
    try:
        t = int(input())
        for _ in range(t):
            inp = list(map(int, input().split()))
            n, k = inp[0], inp[1]
            n = n-k
            n = n+k-1
            print(ncr(n, k-1))

    except Exception as _:
        pass


if __name__ == "__main__":
    main()
