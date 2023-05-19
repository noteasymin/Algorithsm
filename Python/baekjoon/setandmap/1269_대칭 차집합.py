A, B = map(int, input().split())
set_a = set
set_b = set

s = list(map(int, input().split()))

set_a = set(s)

s = list(map(int, input().split()))

set_b = set(s)

a = set_a - set_b
b = set_b - set_a

print(len(a)+len(b))