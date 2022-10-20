import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and graph[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny, h)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for i in range(max(map(max, graph))):
    visited = [[False] * N for i in range(N)]
    safe = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and not visited[j][k]:
                safe += 1
                visited[j][k] = True
                dfs(j, k, i)
    ans = max(ans, safe)

print(ans)