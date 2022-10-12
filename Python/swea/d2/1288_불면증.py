T = int(input())

for i in range(1,T+1):
    N = input()
    print(N)
    num_lst = []
    final = [0,1,2,3,4,5,6,7,8,9]
    cnt = 1
    next_N = 0
    while True:

        if set(num_lst) == set(final):
            print(next_N)
            break

        temp = list(map(int, str(next_N)))

        num_lst.extend(temp)
        num_lst = set(num_lst)
        num_lst = list(num_lst)
        print(num_lst)
        next_N = str(int(N) * cnt)
        cnt += 1




