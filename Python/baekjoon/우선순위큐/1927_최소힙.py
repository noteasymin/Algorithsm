from heapq import *
import sys
input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    num = int(input())

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap,num)
    print(heap)