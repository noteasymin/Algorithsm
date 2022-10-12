T = int(input())
cnt = 0
for _ in range(T):
    num_lst = list(map(int,input().split()))
    max_num = max(num_lst)
    print(f'#{cnt} {max_num}')

