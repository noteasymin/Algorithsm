import sys

input = sys.stdin.readline


def solution():
    W, N = map(int, input().split())

    jewels = [list(map(int, input().split())) for _ in range(N)]

    jewels.sort(key=lambda x: x[1], reverse=True)

    answer = 0
    print(jewels)
    for weight, price in jewels:
        if W > weight:
            answer += weight * price
            W -= weight

        else:
            answer += W * price
            break


solution()
