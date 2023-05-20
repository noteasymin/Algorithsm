def solution():
    t = int(input())

    for i in range(1, t + 1):
        lst = list(map(int, input().split()))
        lst.sort()
        answer = round(sum(lst[1:-1]) / 8)
        print(f'#{i} {answer}')


solution()
