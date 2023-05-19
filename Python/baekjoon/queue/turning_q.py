from collections import deque
import sys


queue = deque()

N, M = map(int,sys.stdin.readline().split())

for i in range(N):
    queue.append(i+1)
print(queue)