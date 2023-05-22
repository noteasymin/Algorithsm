import math


def solution():
    t = int(input())

    for i in range(t):
        n, m = map(int, input().split())

        bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
        print(bridge)


solution()
