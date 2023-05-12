import sys
import itertools

input = sys.stdin.readline


def solution():
    m, n, k = map(int, input().split())
    secret_menu = list(map(int, input().split()))
    check = 0
    if m > n:
        print("normal")
        exit()
    order = list(map(int, input().split()))

    order = list(set(itertools.permutations(order, m)))

    for i in order:
        if secret_menu == list(i):
            check = 1
            break

    if check == 1:
        print("secret")
    else:
        print("normal")


solution()
