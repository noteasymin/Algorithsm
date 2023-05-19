import sys

List = []

for i in range(0,9):
    List.append(sys.stdin.readline())

List =list(map(int,List))

print(max(List))
print(List.index(max(List))+1)
