def rev(board):
    x,y = map(int, input().split())
    x = x - 1
    y = y - 1

    for i in range(19):
        if board[x][i] == 1:
            board[x][i] = 0
        elif board[x][i] == 0:
            board[x][i] = 1
        
        if board[i][y] == 1:
            board[i][y] = 0
        elif board[i][y] == 0:
            board[i][y] = 1
        
board = [list(map(int, input().split())) for _ in range(19)]
n = int(input())

for i in range(n):
    rev(board)

for i in range(19):
    for j in range(19):
        print(board[i][j], end = " ")
    print()
