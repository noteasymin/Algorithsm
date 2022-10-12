cnt1 = 0
cnt2 = 0

def fib(n):
    global cnt1
    cnt1 += 1

    if n == 1 or n == 2:
        cnt1 -= 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt2
    cnt2 += 1
    f[1], f[2] = 1, 1

    for i in range(3, n):
        cnt2+=1
        f[i] = f[i-1] + f[i-2]
    return f[n]
f = [0 for _ in range(41)]
n = int(input())
fib(n)
fibonacci(n)
print(cnt1+1,cnt2)