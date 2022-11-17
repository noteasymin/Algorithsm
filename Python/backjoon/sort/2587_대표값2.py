lst = []
for i in range(5):
    lst.append(int(input()))

lst = sorted(lst)
print(sum(lst) // 5)
print(lst[2])