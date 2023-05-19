def dice():
    C = S = 100
    cnt = int(input())

    for i in range(cnt):
        num1, num2 = map(int,input().split(" "))

        if num1 > num2:
            S = S - num1
        elif num2 > num1:
            C = C - num2
        else:
            pass
    
    print(C)
    print(S)
dice()