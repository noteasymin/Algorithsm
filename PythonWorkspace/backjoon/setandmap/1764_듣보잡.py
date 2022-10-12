import sys


def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    arr1 = set()
    arr2 = set()

    for _ in range(N + M):
        if _ < N:
            arr1.add(input())
        else:
            arr2.add(input())

    result = sorted(list(arr1 & arr2))
    print(len(result))
    for i in result:
        print(i.rstrip())


solution()