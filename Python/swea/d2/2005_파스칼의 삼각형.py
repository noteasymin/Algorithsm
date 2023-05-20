def solution():
    T = int(input())
    for tc in range(1, T + 1):
        n = int(input())

        answer = []

        for i in range(n):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(answer[i - 1][j] + answer[i - 1][j - 1])

            answer.append(temp)
        print(f'#{tc}')
        for i in answer:
            print(*i)


solution()
