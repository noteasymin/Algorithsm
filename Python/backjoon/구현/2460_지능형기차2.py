max_cus = 0
train = 0
for i in range(10):
    a, b = map(int, input().split())
    train += b
    train -= a

    if max_cus < train:
        max_cus = train

print(max_cus)