T = int(input())

cnt = 1

for _ in range(T):
    num_lst = list(map(int,input().split()))
    N = len(num_lst)
    num_lst = sum(num_lst)
    num_lst = num_lst / N
    num_lst = round(num_lst)
    print(f'#{cnt} {num_lst}')
    cnt += 1