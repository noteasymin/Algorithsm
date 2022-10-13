import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, N, M, graph):
    # 이동할 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현 위치에서 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽에 부딪히면 안되기에 조건 확인
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    print(graph[N-1][M-1])

def solution():
    N, M = map(int, input().split())

    graph = []

    for i in range(N):
        graph.append(list(map(int,input().rstrip())))

    bfs(0 ,0, N, M, graph)

solution()