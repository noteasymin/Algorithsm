a = int(input())
b = int(input())
b1 = b % 10
b2 = (b // 10) - ((b//100)*10)
b3 = b // 100
print(a*b1)
print(a*b2)
print(a*b3)
print(a*b)