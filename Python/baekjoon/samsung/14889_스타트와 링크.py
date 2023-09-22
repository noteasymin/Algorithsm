import sys

N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
player = [False for _ in range(N)]
minValue = N // 2 * (N // 2 - 1) * 100


def get_ans():
    global minValue
    s_result = 0
    l_result = 0

    sTeam = [idx for idx, val in enumerate(player) if val == True]
    lTeam = [idx for idx, val in enumerate(player) if val == False]
    for i in range(0, N // 2):
        for j in range(i + 1, N // 2):
            s_first = sTeam[i]
            s_second = sTeam[j]
            s_result += stat[s_first][s_second] + stat[s_second][s_first]

            l_first = lTeam[i]
            l_second = lTeam[j]
            l_result += stat[l_first][l_second] + stat[l_second][l_first]

    minValue = min(minValue, abs(s_result - l_result))


def dfs(depth, idx):
    if depth == N / 2:
        get_ans()
        return
    for i in range(idx, N):
        if player[i]:
            continue

        player[i] = True
        dfs(depth + 1, i)
        print(player)
        player[i] = False
        print(player)


dfs(0, 1)
print(minValue)
