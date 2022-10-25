arr = []
max_num = -1

for i in range(9):
    temp = list(map(int, input().split()))
    if max_num < max(temp):
        max_num = max(temp)
        loc = i
    arr.append(temp)

print(max_num)
print(loc + 1, arr[loc].index(max_num) + 1)