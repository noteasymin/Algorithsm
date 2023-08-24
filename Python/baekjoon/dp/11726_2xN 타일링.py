def solution():
    n = int(input())
    mem = [0] * 1001

    mem[1] = 1
    mem[2] = 2

    for i in range(3, 1001):
        mem[i] = (mem[i - 1] + mem[i - 2]) % 10007

    print(mem[n])


solution()
