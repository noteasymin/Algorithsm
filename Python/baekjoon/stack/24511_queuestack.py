import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n = int(input())
    seq = deque(map(int, input().split()))
    in_arr = deque(map(int, input().split()))
    m = int(input())
    m_seq = deque(map(int, input().split()))
    arr = deque()
    ans = deque()

    for i in range(len(seq)):
        if seq[i] == 0:
            arr.append(in_arr[i])

    for i in m_seq:
        arr.appendleft(i)

    for i in range(len(m_seq)):
        print(arr.pop(), end=" ")


solution()
