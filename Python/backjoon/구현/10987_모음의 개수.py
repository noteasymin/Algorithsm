lst = ['a','e','i','o','u']

s = input()
result = 0

for i in lst:
    result += s.count(i)

print(result)