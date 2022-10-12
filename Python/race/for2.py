c = 0
def cnt():
    global c
    for_c = 0
    for_w = 0
    s = input()

    for_c = s.count('for')
    for_w = s.count('while')

    if c < for_c + for_w:
        c = for_c + for_w

co = int(input())
for i in range(co):
    cnt()
print(c)
