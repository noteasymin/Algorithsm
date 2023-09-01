import sys

sys.setrecursionlimit(10 ** 8)

N = int(input())
village = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# def dfs(x, y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]  # 상 하 좌 우
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < N and 0 <= ny < N and village[nx][ny] == 1:
#             village[nx][ny] = 0
#             dfs(nx, ny)
#
#
def dfs(i, j):
    stack = [(i, j)]

    while stack:
        y, x = stack.pop()

        if not village[y][x]:
            continue

        village[y][x] = 0

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if ny in (-1, N) or nx in (-1, N) or not village[ny][nx]:
                continue

            stack.append((ny, nx))


for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            answer += 1
            dfs(i, j)

print(answer)
