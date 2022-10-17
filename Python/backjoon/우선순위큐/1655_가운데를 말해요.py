import heapq
import sys
input = sys.stdin.readline

N = int(input())
q1 = []
q2 = []
for i in range(N):
    num = int(input())
    cur = len(q) // 2

    heapq.heappush(q, num)

    if len(q) == 1 or len(q) == 2:
        print(q[0])
        continue

    print(q,cur)

    if len(q) % 2 != 0:
        print(q[cur])
    else:
        print(q[cur-1])

    cur += 1