from collections import deque


def solution():
    n, m = map(int, input().split())

    lst = deque([i for i in range(1, n + 1)])
    print(lst)

    for _ in range(m):
        i, j, k = map(int, input().split())
        i -= 1
        j -= 1

        for _ in range(k):
            lst.insert()



solution()