def solution():
    n, b = map(int, input().split())
    print(convert(n, b))


def convert(n, b):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, b)
        if mod >= 10:
            mod = chr(mod + 55)
        rev_base += str(mod)

    return rev_base
    # 역순인 진수를 뒤집어 줘야 원래 변환하고자 하는 base가 출력


solution()
