import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperature = list(map(int,input().split()))

part_sum = sum(temperature[:K])
answer = [part_sum]

for i in range(0, len(temperature) - K):
    part_sum = part_sum - temperature[i] + temperature[i+K]
    answer.append(part_sum)

print(max(answer))