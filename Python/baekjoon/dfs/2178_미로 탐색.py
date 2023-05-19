from collections import deque

def bfs(x, y):

    queue = deque()
    queue.append((x,y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

N, M = map(int, input().split())
graph = [[] for i in range(N)]

for i in range(N):
    graph[i] = list(map(int, input()))

print(bfs(0, 0))