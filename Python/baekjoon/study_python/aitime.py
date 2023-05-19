def ai():
    h, m, s = map(int,input().split())
    while True:
        if h >= 24:
            h = h - 24
        elif m >= 60:
            m = m - 60
            h = h + 1
        elif s >= 60:
            s = s - 60
            m = m + 1
        else:
            break

    timer = int(input())
    s = s + timer

    while True:
        if h >= 24:
            h = h - 24
        elif m >= 60:
            m = m - 60
            h = h + 1
        elif s >= 60:
            s = s - 60
            m = m + 1
        else:
            break
ai()