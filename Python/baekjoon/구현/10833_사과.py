import sys
input = sys.stdin.readline

N = int(input())
lst = []
answer = 0
for i in range(N):
    apple = list(map(int,input().split()))
    lst.append(apple)

for i in lst:
    if i[0] > i[1]:
        answer += i[1]
    else:
        temp = i[1] // i[0]
        answer += i[1] % (i[0] * temp)


print(answer)