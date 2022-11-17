def solution(board):
    for i in board:
        first_check = []
        for j in range(9):
            if i[j] == '.':
                pass
            elif i[j] in first_check:
                print('false')
                return False
            else:
                first_check.append(i[j])

    for i in range(9):
        second_check = []
        for j in board:
            if j[i] == '.':
                pass
            elif j[i] in second_check:
                print('false')
                return False
            else:
                second_check.append(j[i])
    row, col = 3, 3
    for i in range(3):
        third_check = []
        for j in range(row - 3,row):
            for k in range(col - 3 ,col):
                if board[j][k] == '.':
                    pass
                elif board[j][k] in third_check:
                    print('false')
                    return False
                else:
                    third_check.append(board[j][k])


        row += 3
    col += 3
    row = 3
    for i in range(3):
        third_check = []
        for j in range(row - 3,row):
            for k in range(col - 3 ,col):
                if board[j][k] == '.':
                    pass
                elif board[j][k] in third_check:
                    print('false')
                    return False
                else:
                    third_check.append(board[j][k])

        row += 3
    col += 3
    row = 3
    for i in range(3):
        third_check = []
        for j in range(row - 3,row):
            for k in range(col - 3 ,col):
                if board[j][k] == '.':
                    pass
                elif board[j][k] in third_check:
                    print('false')
                    return False
                else:
                    third_check.append(board[j][k])

        row += 3

    print('true')





board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

solution(board)