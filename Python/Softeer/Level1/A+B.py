import sys

input = sys.stdin.readline


def solution():
    T = int(input())

    for i in range(1, T + 1):
        a, b = map(int, input().split())
        print(f'Case #{i}: {a + b}')


solution()
