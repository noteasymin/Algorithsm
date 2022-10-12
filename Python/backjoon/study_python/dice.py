from dataclasses import replace


def dice():

    num = list(map(int,input().split()))
    num = sorted(num)
    
    if num[0] == num[1] and num[1] == num[2]:
        print(10000 + num[0] * 1000)
    elif num[0] == num[1] or num[0] == num[2]:
        print(1000 + num[0] * 100)
    elif num[1] == num[2]:
        print(1000 + num[1] * 100)
    else:
        print(max(num)*100)


dice()