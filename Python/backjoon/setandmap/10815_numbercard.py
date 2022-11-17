import sys

N = int(sys.stdin.readline())

num_lst = set(map(int,sys.stdin.readline().split()))

print(num_lst)

M = int(sys.stdin.readline())

num_lst2 = []

num_lst2 = list(map(int,sys.stdin.readline().split()))


for i in num_lst2:
    if i in num_lst:
        print(1,end=" ")
    else:
        print(0,end=" ")