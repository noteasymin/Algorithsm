from collections import deque

N, K, Q = map(int, input().split())
graph = deque()
for _ in range(N):
    graph.append(list(map(str, input())))

for _ in range(Q):
    y, x, d = map(str, input().split())
    y = int(y) - 1
    x = int(x) - 1
    graph[y][x] = d

    for i in graph:
        print(i)
    print('---------------')
