N, M = map(int, input().split())
arr = [[[0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    # 직선을 그리기 시작하는 위치와 방향을 입력받기
    y, x, d = input().split()

    y = int(y) - 1
    x = int(x) - 1

    if d == 'R':
        for j in range(x, N):
            arr[y][j][1] += 1
    elif d == "L":
        for j in range(x + 1):
            arr[y][j][1] += 1
    elif d == "U":
        for i in range(y + 1):
            arr[i][x][0] += 1
    elif d == "D":
        for i in range(y, N):
            arr[i][x][0] += 1

result = 0

for i in range(N):
    for j in range(N):
        result += arr[i][j][0] * arr[i][j][1]

print(result)
