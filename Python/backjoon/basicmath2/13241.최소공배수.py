def solution():
    a, b = map(int, input().split())
    res = a * b

    # 최대공약수 (유클리드)
    while b:
        if a > b:
            a, b = b, a

        b %= a

    #최소 공배수
    print(res // a)

solution()
