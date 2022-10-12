def move():
    cnt = int(input())
    moving = input().split(" ")
    r = []
    c = []
    you = [1,1]
    for i in range(cnt):
        r.append(i+1)
        c.append(i+1)

    for i in moving:
        if i == 'U':
            you[0] -= 1
            if you[0] not in c:
                you[0] += 1
                continue
        elif i == 'D':
            you[0] += 1
            if you[0] not in c:
                you[0] -= 1
                continue
        
        elif i == 'R':
            you[1] += 1
            if you[1] not in r:
                you[1] -= 1
                continue
        elif i == 'L':
            you[1] -= 1
            if you[1] not in r:
                you[1] += 1
                continue

    print(you)
            
move()