def solution():
    a, b = map(int, input().split())
    res = a * b

    # 최대공약수 (유클리드)
    while b:
        if a > b:
            a, b = b, a

        b %= a

    print(res // a)

solution()
