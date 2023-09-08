from collections import deque

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (N + 1)


def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()

        visited[now] = 1

        for to in sorted(graph[now]):
            if not visited[to]:
                q.append(to)
                break
        else:
            return now


result = bfs(K)
print(sum(visited), result)
