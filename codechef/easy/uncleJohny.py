# cook your dish here
from sys import stdin

try:
    testcases = int(stdin.readline())
    for _ in range(testcases):
        input_len = int(stdin.readline())
        numbers = list(map(int, stdin.readline().split()))
        el_idx = int(stdin.readline())
        el = numbers[el_idx - 1]
        numbers.sort()
        print(numbers.index(el) + 1)

except ValueError as e:
    pass
