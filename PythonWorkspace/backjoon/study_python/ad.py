def ad():
    r, e, c = map(int,input().split(" "))

    e = e - c
    if e > r:
        print('advertise')
    elif e == r:
        print('does not matter')
    else:
        print('do not advertise')
    
for i in range(int(input())):
    ad()