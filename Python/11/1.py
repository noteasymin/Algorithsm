# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


def solution(S):
    N = len(S)
    count = 0
    new_s = deque(S)

    for i in range(N - 1):
        if new_s[0] == new_s[-1]:
            count += 1

        new_s.append(new_s.pop())

    print(count)


solution('abbaa')
