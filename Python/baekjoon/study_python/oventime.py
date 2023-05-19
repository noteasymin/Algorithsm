def timer():
    h,m = map(int,input().split())

    while True:
        if h >= 24:
            h = h - 24
        elif m >= 60:
            m = m - 60
            h = h + 1
        else:
            break
    
    timer = int(input())
    m = m + timer

    while True:
        if h >= 24:
            h = h - 24
        elif m >= 60:
            m = m - 60
            h = h + 1
        else:
            break
    
    print(h,m)
timer()