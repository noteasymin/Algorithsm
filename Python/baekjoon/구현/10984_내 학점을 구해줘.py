T = int(input())

for i in range(T):
    N = int(input())
    total_c = 0
    total_g = 0
    for _ in range(N):
        C, G = map(float, input().split())
        total_c += C
        total_g += G * C

    print(int(total_c), round(total_g/total_c,1))