def solution():
    n, m = map(int, input().split())
    lst = [i for i in range(1, n + 1)]

    for _ in range(m):
        i, j = map(int, input().split())

        temp = lst[i-1]
        lst[i-1] = lst[j-1]
        lst[j-1] = temp

    for i in lst:
        print(i, end=" ")


solution()