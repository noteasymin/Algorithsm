from collections import deque

T = int(input())

for i in range(1, T+1):
    A = deque(map(int, input().split()))
    B = deque(map(int, input().split()))
    max_value_lst = deque()

    while len(A) != len(B):
        loc = 0
        max_value = 0
        if len(A) < len(B):
            for j in A:
                max_value += j * B[loc]
                loc += 1
                if loc+len(A) == len(B):
                    break
            max_value_lst.append(max_value)
            print(max_value_lst)

        elif len(B) < len(A):
            for j in B:
                max_value += j * A[loc]
                loc += 1
                if loc + len(B) == len(A):
                    break
            max_value_lst.append(max_value)
            print(max_value_lst)
    print(max(max_value_lst))
