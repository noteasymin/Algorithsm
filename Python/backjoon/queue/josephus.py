from collections import deque

N, K = map(int, input().split())

people = [i+1 for i in range(N)]
lst = []

while people:
    print(people)
    print(people.pop(K-1))
    K += K

print(lst)
