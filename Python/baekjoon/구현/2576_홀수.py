lst = []
for i in range(7):
    lst.append(int(input()))

result = []
for i in lst:
    if i % 2 != 0:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))