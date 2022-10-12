def chess():
    r, c = map(int, input().split())
    i = j = 0
    board = []
    cnt = 0
    for i in range(r):
        word = list(input())
        board.append(word)

    for i in range(r):
        if i+1 >= r:
            break
        for j in range(c):
            if j+1 >= c:
                break
            elif board[i+1][j] != board[i][j] or board[i-1][j] != board[i][j] or board[i][j+1] != board[i][j] or board[i][j-1] != board[i][j]:
                continue
            else:
                cnt += 1
    print(cnt)
chess()