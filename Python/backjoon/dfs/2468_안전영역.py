import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, h):
    print(visited)

    if graph[x][y] > h:
        visited[x][y] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, h)
    return False



N = int(input())
graph = [[]] * N
visited = [[False for i in range(N)] for j in range(N)]

for i in range(N):
    h = list(map(int, input().split()))
    graph[i] = h

#for i in range(0,101):
    #visited = [[]]
    #dfs(0, 0, i)

dfs(0, 0, 1)

print(visited)