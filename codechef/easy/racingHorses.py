# cook your dish here
from sys import stdin


def get_min_diff_set(numbers, input_len):
    numbers.sort()
    ans = numbers[1] - numbers[0]
    for idx in range(input_len-1):
        temp = numbers[idx + 1] - numbers[idx]
        if ans > temp:
            ans = temp
    return ans


try:
    testcases = int(stdin.readline())
    for _ in range(testcases):
        input_len = int(stdin.readline())
        numbers = list(map(int, stdin.readline().split(' ')))
        print(get_min_diff_set(numbers, input_len))

except Exception as e:
    pass
