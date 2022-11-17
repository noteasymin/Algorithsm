import math


def not_self_number() -> list:
    sum = 0
    
    not_self_number = []
    for i in range(1,10000):
        if i >= 1000:
            sum = i + (i%10) + (math.floor(i/10) % 10) + (math.floor(i/100) % 10) + (math.floor(i/1000) % 10)
            not_self_number.append(sum)
            continue
        elif i >= 100 and i <= 999:
            sum = i + (i%10) + (math.floor(i/10) % 10) + (math.floor(i/100) % 10)
            not_self_number.append(sum)
            continue
        elif i >= 10 and i <= 99:
            sum = i + i%10 + (math.floor(i/10) % 10)
            not_self_number.append(sum)
            continue
        else:
            sum = i + (i%10)
            not_self_number.append(sum)
            continue
        
    return not_self_number

self_number = []
not_self_number = set(not_self_number())
not_self_number = list(not_self_number)

for i in range(1,10000):
    self_number.append(i)


for i in not_self_number:
    if i > 9999:
        continue
    self_number.remove(i)

for i in self_number:
    print(i)