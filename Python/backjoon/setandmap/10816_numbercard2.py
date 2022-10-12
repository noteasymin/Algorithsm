import sys

input = sys.stdin.readline

N = int(input())

num_lst = list(map(int, input().split()))

M = int(input())

num_lst2 = list(map(int, input().split()))

num_lst = sorted(num_lst)


def BS(i, num_lst, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    cnt = 0

    if i > num_lst[mid]:
        return BS(i, num_lst, mid + 1, end)

    elif i < num_lst[mid]:
        return BS(i, num_lst, start, mid - 1)

    elif i == num_lst[mid]:
        for j in range(start, end+1):

            if i == num_lst[j]:
                cnt += 1
    if cnt > 0:
        num_lst.remove(i)

    return cnt


result = []

for i in num_lst2:
    start = 0
    end = N - 1
    result.append(BS(i, num_lst, start, end))

for i in result:
    print(i,end=" ")

