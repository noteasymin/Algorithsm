# 1, 1, 1, 2, 2, 3, 4, 5, 7
# p[4] = p[1] + p[2]
# p[5] = p[2] + p[3]
# p[6] = p[3] + p[4]
# p[7] = p[4] + p[5]
def solution():
    t = int(input())
    p = [1, 1, 1]

    for i in range(3, 101):
        p.append(p[i - 3] + p[i - 2])

    for _ in range(t):
        n = int(input())
        print(p[n - 1])


solution()
