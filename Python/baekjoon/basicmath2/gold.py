def gold():
    n = int(input())
    arr = is_prime_num(n)
    prime_arr = []
    for i in range(len(arr)):
        if arr[i] == True:
            prime_arr.append(i)
    
    while True:
        


def is_prime_num(n):
    arr = [True] * (n+1)

    for i in range(2, n+1):
        if arr[i] == True:
            j = 2
        
        while (i*j) <= n:
            arr[i*j] = False
            j += 1
    return arr


c = int(input())
for i in range(c):
    gold()