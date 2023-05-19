n = int(input())

for i in range(n):
    dic = {}
    p = int(input())

    for j in range(p):
        a, b = input().split()
        a = int(a)

        dic[a] = b


    answer = [v for k,v in dic.items() if max(dic.keys()) == k]

    print(answer[0])