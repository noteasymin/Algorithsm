lst = []
for i in range(5):
    a, b, c, d = map(int, input().split())
    lst.append(a+b+c+d)

print(lst.index(max(lst)) + 1, max(lst))