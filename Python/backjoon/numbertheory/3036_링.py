import math
N = int(input())

lst = list(map(int, input().split()))
num = lst[0]
del lst[0]

for i in lst:
    if num % i == 0:
        answer = num // i
        print(f'{answer}/1')
    else:
        answer = math.lcm(num, i)
        ans1 = answer // i
        ans2 = answer // num
        print(f'{ans1}/{ans2}')