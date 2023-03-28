from collections import deque


def solution():
    lst = deque()
    length = 0

    for _ in range(5):
        s = input()
        length += len(s)
        lst.append(s)
    print(length)




solution()