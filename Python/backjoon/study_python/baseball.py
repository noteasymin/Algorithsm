def baseball():
    Y = K = 0
    sum_Y = sum_K = 0
    for i in range(9):
        score_Y, score_K = map(int,input().split(" "))
        sum_Y += score_Y
        sum_K += score_K
    
    if sum_Y > sum_K:
        print('Yonsei')
    elif sum_Y < sum_K:
        print('Korea')
    else:
        print("Draw")

cnt = int(input())
for i in range(cnt):
    baseball()
        