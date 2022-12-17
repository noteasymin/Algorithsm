T = int(input())

for i in range(T):
    lst = list(map(int, input().split()))
    lst2 = []
    result = 0
    for j in lst:
        if j % 2 == 0:
            result += j
            lst2.append(j)
    print(result,min(lst2))