from collections import deque
import sys

def josephus():
    N, K = map(int,sys.stdin.readline().split())
    J = deque(i+1 for i in range(N))
    new_J = deque()
    cnt = -1 + K
    while True:
        new_J.append(J[cnt])
        del J[cnt]

        cnt += K

        if cnt > len(J):
            




josephus()