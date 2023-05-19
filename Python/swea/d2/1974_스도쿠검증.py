def sudoku(arr):
    for i in range(9):

        # 숫자에 해당하는 idx에 1 추가
        # 요소에 숫자가 2 이상인 것이 있으면 스도쿠 x

        # 가로 거사
        lst_h = [0] * 10

        # 세로 검사
        lst_v = [0] * 10

        for j in range(9):
            # 가로 검사
            lst_h[arr[i][j]] += 1
            if lst_h[arr[i][j]] == 2:
                return 0

            # 세로 검사
            lst_v[arr[j][i]] += 1
            if lst_v[arr[j][i]] == 2:
                return 0

    # 3*3 검사
    # x, y 3*3 스도쿠 검사의 시작점

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            lst = [0] * 10
            for i in range(3):
                for j in range(3):
                    lst[arr[x + i][y + j]] += 1
                    if lst[arr[x + i][y + j]] == 2:
                        return 0
    return 1


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T + 1):
    # 스도쿠
    arr = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, sudoku(arr)))
