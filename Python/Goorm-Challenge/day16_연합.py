from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)

result = 0

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

for i in range(1, N + 1):
    if visited[i]:
        continue

    q = deque([i])
    result += 1
    visited[i] = 1

    while q:
        now = q.popleft()

        for to in graph[now]:
            if not visited[to] and now in graph[to]:
                q.append(to)
                visited[to] = 1


print(result)

