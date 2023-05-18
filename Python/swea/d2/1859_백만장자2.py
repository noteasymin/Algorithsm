T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    N_list = list(map(int, input().split()))

    max_value = N_list[-1]

    profit = 0

    for i in range(N - 2, -1, -1):

        if N_list[i] >= max_value:
            max_value = N_list[i]

        else:
            profit += max_value - N_list[i]

    print('#{} {}'.format(tc, profit))
