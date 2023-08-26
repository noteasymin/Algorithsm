def solution():
    n = int(input())
    roads = list(map(int, input().split()))
    price = list(map(int, input().split()))
    low = price[0]
    answer = roads[0] * low

    for i in range(1, len(roads)):
        if low > price[i]:
            low = price[i]
        answer += low * roads[i]

    print(answer)


solution()
