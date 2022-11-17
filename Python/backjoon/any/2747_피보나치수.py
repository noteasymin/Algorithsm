
lst = [0, 1]
cnt = 2

for i in range(50):
    lst.append(lst[cnt-2] + lst[cnt-1])
    cnt += 1


N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    print(lst[N])