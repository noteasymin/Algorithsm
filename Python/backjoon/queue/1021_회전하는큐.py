from collections import deque

def rotateRight(lst):
    lst.append(lst[0])
    lst.popleft()

def rotateLeft(lst):
    lst.appendleft(lst[-1])
    lst.pop()

N, M = map(int, input().split())
find = list(map(int, input().split()))
lst = [i for i in range(1,N+1)]
lst = deque(lst)
cnt = 0
for i in find:
    cur = lst.index(i)
    a = abs(0 - cur)
    b = abs(len(lst) - cur)

    if cur == 0:
        lst.popleft()
        continue
    elif a < b:
        for i in range(a):
            rotateRight(lst)
            cnt += 1
    else:
        for i in range(b):
            rotateLeft(lst)
            cnt += 1
    lst.popleft()

print(cnt)