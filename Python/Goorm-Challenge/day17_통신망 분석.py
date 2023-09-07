from collections import deque


def bfs(start):
    q = deque([start])

    component = set()

    while q:
        now = q.popleft()

        if visited[now]:
            continue

        visited[now] = 1
        component.add(now)

        for to in graph[now]:
            if not visited[to]:
                q.append(to)

    edge = 0

    for i in component:
        for to in graph[i]:
            if to in component:
                edge += 1
    return sorted(list(component)), edge / len(component)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result, density = [], 0

for i in range(1, N + 1):
    if not visited[i]:
        temp, tempDensity = bfs(i)

    if abs(tempDensity - density) < 1e-8:
        if len(result) > len(temp):
            result = temp
            density = tempDensity
        elif len(result) == len(temp):
            if temp[0] < result[0]:
                result = temp
                density = tempDensity

    elif tempDensity > density:
        result = temp
        density = tempDensity

print(*result)
