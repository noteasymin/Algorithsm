def sumdiv():
    global cnt
    N = int(input())
    num_lst = list(map(int,input().split()))
    answer = 0

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            answer += num_lst[i] % num_lst[j]

    print(f'#{cnt} {answer}')
    cnt += 1


T = int(input())
cnt = 1
for _ in range(T):
    sumdiv()