K, N = map(int, input().split())
lst = []
for i in range(K):
    lst.append(int(input()))
start = 1
end = max(lst)

while start <= end:
    mid = (start + end) // 2

    lan = 0 # 랜 갯수

    for i in lst:
        if i >= mid:
            lan += i // mid

    if lan >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)