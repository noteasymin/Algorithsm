H,M = map(int,input().split())


if(H == 0):
    H = 24

if(M >= 45):
    M = M - 45
else:
    H = H - 1
    M = M + 15

if(H == 24):
    H = 0
    
print(H,M)