import sys
from itertools import combinations

input = sys.stdin.readline


def solution():
    n = int(input())
    candy = list(map(int, input().split()))
    candy_lst = []
    answer = []
    check = 0
    for i in range(1, n + 1):
        candy_lst.append(list(combinations(candy, i)))

    for i in candy_lst:
        for j in i:
            answer.append(sum(j))

    answer.sort(reverse=True)

    for i in answer:
        if i % 2 == 0:
            print(i)
            check = 1
            break

    if check == 0:
        print(0)


solution()
