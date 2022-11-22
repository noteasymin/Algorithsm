N = int(input())
a = 0
for i in range(1,N+1):
    print(' '* a + '*' * (2*N-1))
    a += 1
    N-= 1