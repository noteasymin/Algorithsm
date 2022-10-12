import copy
import sys

# def solution():
#     input = sys.stdin.readline
#     cnt = int(input())
#
#
#     lst = list(map(int,input().split()))
#     chk_lst = list(set(copy.deepcopy(lst)))
#     result = []
#
#     for i in range(cnt):
#         index = 0
#         for j in range(len(chk_lst)):
#             if lst[i] > chk_lst[j]:
#                 index += 1
#         result.append(str(index))
#     result = " ".join(result)
#     print(result)
# solution()

def solution():
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int,input().split()))

    arr2 = sorted(list(set(arr)))

    dic = {arr2[i] : i for i in range(len(arr2))}

    for i in arr:
        print(dic[i],end = ' ')

solution()