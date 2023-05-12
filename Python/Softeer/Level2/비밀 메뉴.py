import sys
import itertools

input = sys.stdin.readline


def solution():
    m, n, k = map(int, input().split())

    if m > n:
        print("normal")
        exit()

    secret = "".join(list(map(str, input().split())))
    menu = "".join(list(map(str, input().split())))

    if secret in menu:
        print("secret")
    else:
        print("normal")


solution()
