import sys

input = sys.stdin.readline


def solution():
    result = 0

    for i in range(5):
        a, b = map(str, input().split())
        a_minute = int(a[:2]) * 60 + int(a[3:5])
        b_minute = int(b[:2]) * 60 + int(b[3:5])

        result += b_minute - a_minute

    print(result)


solution()
