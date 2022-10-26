N = int(input())

lst = list(map(int, input().split()))
num = lst[0]
del lst[0]

for i in lst:
    if num % i == 0:
        answer = num // i
        print(f'{answer}/1')