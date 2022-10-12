from collections import Counter

T = int(input())

for _ in range(T):
    cnt = int(input())

    num_lst = list(map(str,input().strip().split()))

    print(f'#{cnt} {Counter(num_lst).most_common(1)[0][0]}')
