from collections import deque


def solution():
    n, m = map(int, input().split())
    lst = deque([i for i in range(1, n + 1)])

    for _ in range(m):
        i, j = map(int, input().split())

        temp = deque()

        for k in range(i-1, j):
            temp.appendleft(lst[k])

        for k in range(i-1, j):
            lst[k] = temp.popleft()

    for k in lst:
        print(k, end=" ")


solution()