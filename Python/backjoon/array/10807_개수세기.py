import sys
from collections import Counter
input = sys.stdin.readline
#
# N = int(input())
# lst = list(map(int, input().split()))
# v = int(input())
#
# print(lst.count(v))

N = int(input())
lst = list(map(int, input().split()))
v = int(input())

counter = Counter(lst)
print(counter[v])