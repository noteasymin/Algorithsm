def plate():
    p = input()
    total = 10
    height = 5
    for i in range(1,len(p)):
        if p[i] != p[i-1]:
            height = 10
            total += height
        else:
            height = 5
            total += height
    print(total)


plate()