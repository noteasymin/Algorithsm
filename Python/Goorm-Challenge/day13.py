N, K = map(int, input().split())

max_num = 0
village = []

for i in range(N):
    temp = list(map(int, input().split()))
    max_temp = max(temp)
    if max_num < max_temp:
        max_num = max_temp

    village.append(temp)

my_dict = {i: 0 for i in range(1, max_num + 1)}

for i in range(N):
    for j in range(N):
        my_dict[village[i][j]] += 1

a = [0, 0]
for i in range(max_num, 0, -1):
    if my_dict[i] > K and a[1] < my_dict[i]:
        a[0] = i
        a[1] = my_dict[i]

print(a[0])
