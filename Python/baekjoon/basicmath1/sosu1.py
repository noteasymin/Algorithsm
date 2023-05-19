import sys
import math
def find(k):
    if k == 1:
        return False
    global cnt
    for i in range(2,int(math.sqrt(k))+1):
        if k % i == 0:
            return False
        else:
            continue
    cnt += 1
    

n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
num_list = set(num_list)

cnt = 0
for i in num_list:
    find(i)

print(cnt)