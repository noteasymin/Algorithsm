n, m, b = map(int, input().split())
ground = []
for i in range(n):
    ground.append(list(map(int,input().split())))

height = 0

ans = 1000000000000000000000000000000

for i in range(257):
    max = 0
    min = 0

    for j in range(n):
        for k in range(m):
            if ground[j][k] < i:
                min += (i - ground[j][k])
            else:
                max += (ground[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue

    time = 2 * max + min
    if time <= ans:
        ans = time
        height = i

print(ans, height)