N = int(input())
cnt = 1
lst = list(map(int, input().split()))
score = 0
for i in lst:
    if i == 0:
        cnt = 1
    elif i == 1:
        score += cnt
        cnt += 1
print(score)