def solution(n, a, b):
    cnt = 1

    while True:
        if abs(a - b) == 1 & min(a, b) % 2 == 1:
            return cnt
        else:
            a = (a + 1) // 2
            b = (b + 1) // 2
        cnt += 1


solution(8, 4, 7)
