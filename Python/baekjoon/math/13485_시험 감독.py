N = int(input())
room = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for i in range(len(room)):
    if room[i] >= B:
        answer += 1
        room[i] -= B
    if room[i] <= 0:
        continue
    if room[i] % C > 0:
        answer += room[i] // C + 1
    else:
        answer += room[i] // C

print(answer)
