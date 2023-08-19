from collections import deque


def solution():
    n = int(input())
    q = deque(map(int, input().split()))
    s = []
    start = 1

    while q:
        if q[0] == start:
            q.popleft()
            start += 1
        elif s and s[-1] == start:
            s.pop()
            start += 1
        else:
            s.append(q.popleft())

    while s:
        if s[-1] != start:
            print("Sad")
            return
        else:
            s.pop()
            start += 1

    print("Nice")


solution()
