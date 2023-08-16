def convert(n, b, base):
    if n >= b:
        convert(n // b, b, base)
        print(base[n % b], end="")
    else:
        print(base[n % b], end="")


def solution():
    n, b = map(int, input().split())
    base = []

    for i in range(b):
        if i < 10:
            base.append(i)
        else:
            base.append(chr(55 + i))

    convert(n, b, base)


solution()
