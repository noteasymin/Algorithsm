a = input()
a = list(a.replace('6','9'))
b = []
x = a.count('9') // 2

for i in range(x):
    a.remove('9')

for i in range(1,10):
    b.append(a.count((str(i))))

print(max(b))