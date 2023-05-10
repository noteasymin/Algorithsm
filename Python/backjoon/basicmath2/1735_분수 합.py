def solution():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    result_lcm = lcm(b, d)

    a *= result_lcm // b
    c *= result_lcm // d

    numerator = a + c
    denominator = result_lcm

    result_gcd = gcd(denominator, numerator)

    numerator //= result_gcd
    denominator //= result_gcd

    print(numerator, denominator)


def gcd(a, b):
    res = a * b

    # 최대 공약수
    while b:
        if a > b:
            a, b = b, a

        b %= a

    return a


def lcm(a, b):
    res = a * b

    while b:
        if a > b:
            a, b = b, a

        b %= a

    return res // a


solution()
