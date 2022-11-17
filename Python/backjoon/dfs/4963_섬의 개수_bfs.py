import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def bfs(x,y):
    visited[x][y] = 1
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    visited = [[0] * w for _ in range(h)]
    answer = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and not visited[x][y]:
                bfs(x,y)
                answer += 1

    print(answer)