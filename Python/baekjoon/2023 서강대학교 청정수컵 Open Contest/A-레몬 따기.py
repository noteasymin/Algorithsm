import sys

input = sys.stdin.readline


def solution():
    n = int(input())

    tree = list(map(int, input().split()))
    max_lemons = 0
    hole = len(tree)

    for i in range(len(tree)):
        lemon = tree[i] - hole
        max_lemons = max(max_lemons, lemon)
        hole -= 1
    print(max_lemons)


solution() 