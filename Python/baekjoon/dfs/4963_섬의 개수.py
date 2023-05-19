def dfs(x, y):
    if graph[x][y] == 0:
        return False

    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= w or ny >= h:
            return False

        if graph[nx][ny] == 0:
            return False


while True:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
        if dfs(0 ,0):
            cnt += 1

