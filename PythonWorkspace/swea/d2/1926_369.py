N = int(input())
lst = [i for i in range(1,N+1)]

new_lst = 0
for i in lst:
    i = str(i)
    new_lst = i.count('3') + i.count('6') + i.count('9')

    if new_lst == 0:
        print(i,end=" ")
    else:
        print('-'*new_lst,end="")
        print('',end=" ")
