import heapq
import sys
input = sys.stdin.readline

N = int(input())
heapr = [] # 최대힙
heapl = [] # 최소힙

for _ in range(N):
    t = int(input())
    if len(heapl) == len(heapr):
        heapq.heappush(heapl, -t)
    else:
        heapq.heappush(heapr, t)

    if heapr and -heapl[0] > heapr[0]:
        tmp = heapq.heappop(heapr)
        tmp2 = -heapq.heappop(heapl)
        heapq.heappush(heapl,-tmp)
        heapq.heappush(heapr,tmp2)
    print(-heapl[0])