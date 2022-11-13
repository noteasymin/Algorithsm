M = int(input())
N = int(input())
lst = []
start = 0
end = 0

for i in range(1,101):
    lst.append(i**2)

for i in lst:
    if i >= M:
        start = lst.index(i)
        break

for i in lst[::-1]:
    if i <= N:
        end = lst.index(i)
        break

if sum(lst[start:end+1]) == 0:
    print(-1)
else:
    print(sum(lst[start:end+1]))
    print(lst[start])