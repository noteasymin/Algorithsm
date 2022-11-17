import sys
input = sys.stdin.readline
def how():
    N = int(input())
    A = list(map(int,input().split()))
    B,C = map(int,input().split())
    total = 0


    for i in range(len(A)):
        if A[i] < B:
            A[i] = 0
            total += 1
        else:
            A[i] -= B
            total += 1
    
    for i in range(len(A)):
        if A[i] % C > 0:
            total += A[i] // C + 1
        else:
            total += A[i] // C

    print(total)



how()

