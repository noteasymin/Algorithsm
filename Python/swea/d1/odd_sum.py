def odd_sum():
    global cnt
    num_lst = list(map(int, input().split()))
    answer = 0
    for i in num_lst:
        if i % 2 == 1:
            answer += i

    print(f'#{cnt} {answer}')
    cnt += 1

T = int(input())
cnt = 1
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    odd_sum()

        # ///////////////////////////////////////////////////////////////////////////////////
