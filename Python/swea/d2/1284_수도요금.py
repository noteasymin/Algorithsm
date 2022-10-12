def A(W, P):
    return W*P

def B(W, Q, R, S):
    if W <= R:
        return Q
    else:
        return Q + (W-R)*S

T = int(input())
cnt = 1
for i in range(T):
    P,Q,R,S,W = map(int,input().split())

    A_company = A(W, P)

    B_company = B(W, Q, R, S)

    if A_company < B_company:
        print(f'#{cnt} {A_company}')
    else:
        print(f'#{cnt} {B_company}')

    cnt += 1
