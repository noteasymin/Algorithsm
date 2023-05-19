import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    n = int(input())
    current = set()
    for i in range(n):
        name, commute = map(str, input().split())
        if commute == 'enter':
            current.add(name)
        else:
            current.remove(name)

    current = deque(sorted(current, reverse=True))
    for i in current:
        print(i)


solution()
