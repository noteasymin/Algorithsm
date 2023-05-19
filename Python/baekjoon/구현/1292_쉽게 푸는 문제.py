A, B = map(int,input().split())
lst = []
for i in range(1000):
    for j in range(1,i+1):
        lst.append(i)

print(sum(lst[A-1:B]))