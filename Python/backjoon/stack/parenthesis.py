def vps():

    p = list(input())
    if len(p) % 2 == 1:
        print("NO")
        return 0
    for j in range(int(len(p)/2)):
        if p[0] == '(':
            if ')' in p:
                p.remove('(')
                p.remove(')')
            else:
                print("NO")
                return 0
        else:
            print("NO")
            return 0
    print("YES")

cnt = int(input())
for i in range(cnt):      
    vps()