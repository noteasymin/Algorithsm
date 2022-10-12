def check():
    global cnt
    puzzle = []
    for i in range(9):
        puzzle.append(list(map(int, input().split())))

    # horizon check
    for i in puzzle:
        if len(set(i)) < 9:
            print(f'#{cnt} 0')
            cnt += 1
            return 0

    # vertical check
    for i in range(9):
        new_array = []
        for j in range(9):
            new_array.append(puzzle[j][i])

        if len(set(new_array)) < 9:
            print(f'#{cnt} 0')
            cnt += 1
            return 0

    cnt_1 = 0
    cnt_2 = 0

    while True:
        for i in range(cnt_1,cnt_1+3):
            for j in range(cnt_2,cnt_2+3):
                print(i,j)
        cnt_2 += 3



T = int(input())
cnt = 1

for _ in range(T):
    check()

