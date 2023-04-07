from collections import deque


def solution():
    n = int(input())
    x = deque()
    y = deque()
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    result = (max(x) - min(x)) * (max(y) - min(y))
    print(result)


solution()