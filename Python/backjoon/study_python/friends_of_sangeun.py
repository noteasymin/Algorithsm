def friends():
    while True:
        M, W = map(int, input().split(" "))
        if M == 0 and W == 0:
            break
        else:
            print(M + W)

friends()