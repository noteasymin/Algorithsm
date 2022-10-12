def calc(A,B):
    global cnt
    quotient = A // B
    remainder = A % B
    print(f'#{cnt} {quotient} {remainder}')
    cnt += 1

T = int(input())
A, B = map(int,input().split())
cnt = 1
for _ in range(T):
    calc(A,B)