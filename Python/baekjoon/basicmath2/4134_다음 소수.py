def solution():
    n = int(input())

    for i in range(n):
        num = int(input())
        if num == 0:
            print(2)
            continue

        while True:
            if is_prime(num):
                print(num)
                break
            num += 1


def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


solution()
