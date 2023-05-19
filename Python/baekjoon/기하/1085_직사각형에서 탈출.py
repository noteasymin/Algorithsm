import sys


def solution():
    input = sys.stdin.readline
    x, y, w, h = map(int,input().split())
    answer = []
    if x >= abs(x - w):
        answer.append(abs(x-w))
    else:
        answer.append(x)

    if y >= abs(y - h):
        answer.append(abs(y - h))
    else:
        answer.append(y)

    print(min(answer))
solution()