T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        YY = str(H)
    else:
        YY = int(N % H)

    if H >= N:
        XX = str(1)
    elif N % H == 0:
        XX = (N // H)
    else:
        XX = (N // H) + 1

    if len(str(XX)) < 2:
        XX = '0' + str(XX)

    print(str(YY) + str(XX))