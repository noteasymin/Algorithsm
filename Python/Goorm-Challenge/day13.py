from collections import deque

# dy/dx 배열을 선언합니다.
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# BFS를 구현할게요.
def bfs(i, j):
    # 큐에 (i, j)를 넣어 선언합니다.
    q = deque([(i, j)])

    # arr을 직접 갱신하며 방문 체크를 해주겠습니다. 따라서 건물의 유형을 미리 저장해둘게요.
    M = arr[i][j]

    # 조건을 만족하는 건물의 개수를 세어서, 단지가 될 수 있는지 확인하기 위해 변수를 선언합니다.
    cnt = 0

    # 큐에 원소가 없을 때까지 반복합니다.
    while q:
        # 큐는 꺼낼 때 왼쪽에서 꺼냅니다!
        y, x = q.popleft()

        # (y, x) 위치가 M이 아니라면 건너뜁니다.
        if arr[y][x] != M:
            continue

        # 처음 방문하는 경우 방문 체크를 해주고 건물의 개수에 1을 더하겠습니다.
        arr[y][x] = 0
        cnt += 1

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 범위 체크 중요합니다! 또한 탐색 위치의 건물 유형이 M과 달라도 건너뛰어줍니다.
            if ny in (-1, N) or nx in (-1, N) or arr[ny][nx] != M:
                continue

            # 조건을 만족하므로 큐에 추가해줍니다.
            q.append((ny, nx))

    return cnt


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 건물의 유형마다 단지 개수를 저장할 배열을 만듭니다.
# M의 범위는 1 <= M <= 30 이므로 31칸을 선언해줄게요.
count = [0] * 31

# 모든 위치에 대해 탐색을 해봅시다.
for i in range(N):
    for j in range(N):
        # arr[i][j] != 0 이면 아직 방문하지 않은 것이므로 탐색을 합니다.
        if arr[i][j]:
            # BFS를 수행하면 arr[i][j]가 0으로 바뀝니다. 바꾸기 전에 미리 M 값을 저장해두겠습니다.
            M = arr[i][j]

            # (i, j)에 대해 BFS를 수행하고 이 단지 후보에 포함된 건물의 개수를 가져옵니다.
            # 이 값이 K 보다 크거나 같으면 하나의 단지가 됩니다.
            # 미리 저장해놨던 M을 이용해, 조건을 만족하면 M번 건물의 유형에 대해 단지 개수를 1 더합니다.
            if bfs(i, j) >= K:
                count[M] += 1

result, temp = 0, 0

for i in range(31):
    if temp <= count[i]:
        result = i
        temp = count[i]

print(result)