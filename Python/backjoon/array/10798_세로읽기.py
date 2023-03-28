from collections import deque


def solution():
    lst = deque()
    new_lst = deque([[] for i in range(15)])
    length = 0

    for _ in range(5):
        s = input()
        for i in range(len(s)):
            new_lst[i].append(s[i])

    for i in range(15):
        print("".join(new_lst[i]), end="")


solution()