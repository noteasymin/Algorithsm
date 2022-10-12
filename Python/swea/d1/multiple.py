T = int(input())
num = 2
for i in range(0,T+1):
    if i == 0:
        print(1,end=' ')
    elif i == 1:
        print(2,end=' ')
    else:
        print(num ** i,end = ' ')