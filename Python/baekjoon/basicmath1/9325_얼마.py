T = int(input())

for i in range(T):
    car = int(input())
    n = int(input())
    for j in range(n):
        a,b = map(int,input().split())
        car += a*b

    print(car)