result = 0

for i in range(12):
    a = float(input())
    a *= 100
    result += a
result = round(result/100, 2)
print(f'${result/12}')