# Bytelandian gold coins - Accepted
memo = {}


def coins(n):

    if n < 10:
        return n
    if n in memo:
        return memo[n]

    c = coins(n//2) + coins(n//3) + coins(n//4)
    memo[n] = max(c, n)
    return memo[n]


def main():
    for _ in range(10):
        try:
            n = int(input())
            print(coins(n))
        except Exception as _:
            return 0


if __name__ == "__main__":
    main()
