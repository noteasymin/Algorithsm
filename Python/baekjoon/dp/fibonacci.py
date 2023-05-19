dic = {}
cnt_1 = 0
cnt_0 = 0
def fibonacci_2(n):
    global cnt_1,cnt_0
    if n in dic:
        return dic[n]

    if n == 0:
        cnt_0 += 1
        dic[0] = 0
        return 0

    elif n == 1:
        cnt_1 += 1
        dic[1] = 1
        return 1
    
    else:
        dic[n] = fibonacci_2(n-1) + fibonacci_2(n-2)
        return print(dic[n],cnt_0,cnt_1)

n = int(input())

for _ in range(n):
    m = int(input())
    fibonacci_2(m)
