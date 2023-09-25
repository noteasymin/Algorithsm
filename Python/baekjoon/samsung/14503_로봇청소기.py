N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
result = 0


def clean(r, c, d):
    global result, N, M

    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while True:

        #print(f'현 위치 r={r} c={c} d={d}')
        #for i in graph:
        #    print(i)
        #print("-----------------")
        if graph[r][c] == 0:
            graph[r][c] = 2
            result += 1
            continue

        flag = 0
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
                flag = 1
                break

        if flag == 1:
            for i in range(4):
                if d == 0:
                    d = 3
                else:
                    d -= 1

                if graph[r + dx[d]][c + dy[d]] == 0:
                    r += dx[d]
                    c += dy[d]
                    break

        else:
            temp_d = d + 2
            if temp_d >= 4:
                temp_d -= 4

            if graph[r + dx[temp_d]][c + dy[temp_d]] != 1:
                r += dx[temp_d]
                c += dy[temp_d]
            else:
                return


clean(r, c, d)
print(result)
