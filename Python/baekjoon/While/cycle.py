import copy

n = int(input()) # 26 -> 68 -> 84 -> 42 -> 26
original = copy.deepcopy(n)
cycle = 0

if n // 10 == 0 : 
    n = n * 11
    cycle += 1

while 1:
    a = n // 10 # 2 
    b = n % 10 # 6 
    sum = a + b  # 8 
    n = b*10 + sum%10 
    cycle += 1
    if n == original: break

print(cycle)