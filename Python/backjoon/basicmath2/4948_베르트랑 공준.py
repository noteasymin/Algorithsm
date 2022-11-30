def prime_list(n):
    # 에라토스테네스의 체 초기화 : n개 요소에 True 설정(소수로 간주)
    sieve = [True] * 246912

    m = int(246912**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, 246912, i):
                sieve[j] = False
    return [i for i in range(n+1, 2*n) if sieve[i] == True]

while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
    else:
        answer = prime_list(n)
        print(len(answer))