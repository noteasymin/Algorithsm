import heapq
from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    a = int(input())

    if a != 0:
        heapq.heappush(q,(abs(a),a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])