def find(board):
    x = 1
    y = 1
    board[x][y] = 9
    while True:
        if board[x][y+1] == 2:
            board[x][y+1] = 9
            break

        if board[x][y+1] == 0:
            board[x][y+1] = 9
            y = y + 1
            continue

        if board[x+1][y] == 2:
            board[x+1][y] = 9
            break

        if board[x+1][y] == 0:
            board[x+1][y] = 9
            x = x + 1
            continue
            
        if ((board[x][y+1] == 1 and board[x+1][y] == 1) or (x == 9 and y == 9)): break
board = [list(map(int,input().split())) for i in range(10)]
find(board)
for a,b,c,d,e,f,g,h,i,j in board:
    print(a,b,c,d,e,f,g,h,i,j)
