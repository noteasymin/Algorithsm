N = int(input())
a = N-1
for i in range(1,N+1):
    print(' '* a + '*' * (2*i-1))
    a -= 1