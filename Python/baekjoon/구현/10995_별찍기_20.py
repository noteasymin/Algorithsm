N = int(input())

for i in range(N):
    for j in range(N):
        if j == 0 and i % 2 != 0:
            print(' ' * (i % 2), end="")
        print('*', end=" ")
    print()