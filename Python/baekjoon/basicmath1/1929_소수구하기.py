def isprime(a):
    if a == 1:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False

        return True


M, N = map(int, input().split())

for i in range(M, N + 1):
    if isprime(i):
        print(i)
